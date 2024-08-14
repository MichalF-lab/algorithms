library(MASS)
library(ggplot2)
set.seed(131311)

# 1.1
generate_Y <- function(p, mu, sigma, n) {
    X <- rbinom(n, 1, p)
    Y <- ifelse(X == 0, rnorm(sum(X == 0), 0, 1),
                rnorm(sum(X == 1), mu, sigma))
    return(Y)
}

p <- 0.9
mu <- 20
sigma <- 3
n <- 1000

Y <- generate_Y(p, mu, sigma, n)
hist(Y, breaks = 30, probability = TRUE)


x <- seq(min(Y), max(Y), length.out = 1000)
mix <- (1 - p) * dnorm(x, 0, 1) + p * dnorm(x, mu, sigma)
lines(x, mix, col = "blue", lwd = 2)

# 1.2
tab <- matrix(nrow = 2, ncol = 0) 
while (length(tab) / 2 <= 1000) {
    x <- runif(1, 0, 1)
    y <- runif(1, 0, 1)

    if (x + y >= 1) {
        next
    }

    gestosc <- 20 * x * y ^ 2

    if (gestosc > runif(1, 0, 1)) {
        tab <- cbind(tab, c(x, y))
    }
}

plot(tab[1,], tab[2,], col = "blue", pch = 16, xlim = c(0, 1), ylim = c(0, 1))


# 1.3
sigmq <- matrix(data = c(2, 2, 0,2, 5, -3,0, -3, 9), nrow = 3, byrow = TRUE)
mi <- c(1,-1,5)
data <- mvrnorm(n = 1000, mu = mi, Sigma = sigmq)

print(all.equal(sigmq, t(sigmq)))
print(all(eigen(sigmq)$values > 0))

cov_matrix <- matrix(c(1, 0.7, 0.7, 1), nrow = 2)
correlated_variables <- mvrnorm(n = 100, mu = c(0, 0), Sigma = cov_matrix)

df <- as.data.frame(data)
names(df) <- c("X1", "X2", "X3")

ggplot(df, aes(x = X1, y = X2, color = X3)) +
    geom_point() +
    scale_color_gradient(low = "blue", high = "red") +
    labs(title = "Próby z rozk³adu wielowymiarowego",
       x = "X1", y = "X2", color = "X3")


# 2.1
denisty_1 <- function(x) {
    return(exp(1) ^ (-(x ^ 2)))
}

approximation <- function(f, n) {
    ext <- c(mean(f(seq(0, 1, length.out = n))),
             var(f(seq(0, 1, length.out = n))),
             sd(f(seq(0, 1, length.out = n))))
    return (ext)
}
print(approximation(denisty_1, 10))
print(approximation(denisty_1, 100))
print(approximation(denisty_1, 1000))

# Przedzia³ ufnoœci
M <- 1000
n <- 100
alpha <- 0.1
tab <- vector("list", M)
for (j in 1:M) {
    U <- runif(n)
    p <- c(sort(denisty_1(U)))
    tab[[j]] <- p
}
#print(tab)

temp <- c()
interval <- c()
for (i in 1:n) {
    for (j in 1:M) {
        temp <- c(temp, tab[[j]][i])
    }
    temp <- sort(temp)
    interval <- c(interval, abs(temp[M - M * alpha] - temp[M * alpha]))
    temp <- c()
}
interval <- mean(interval)
print(interval)

# 2.2
n <- 500000
U <- runif(n)
denisty_2 <- function(x) {
    return((exp(1) ^ (-x))*(x^5)*cos(x))
}
X <- denisty_2((1 / U) - 1) * (y ^ (-2))
print(mean(X))

# 2.3
rr <- 1000
max_iter <- 10000
tt <- 2 
# Generowanie siatki punktów
x <- seq(-2, 2, length.out = rr)
y <- seq(-2, 2, length.out = rr)
grid <- expand.grid(x = x, y = y)
grid$c <- grid$x + 1i * grid$y
grid$in_set <- rep(TRUE, nrow(grid))

# Funkcja sprawdzaj¹ca przynale¿noœæ do zbioru Mandelbrota
mandelbrot <- function(c, max_iter, threshold) {
    z <- 0
    for (k in 1:max_iter) {
        z <- z ^ 2 + c
        if (Mod(z) > threshold) {
            return(FALSE)
        }
    }
    return(TRUE)
}

# Sprawdzanie wszystkich punktów w siatce
for (i in 1:nrow(grid)) {
    grid$in_set[i] <- mandelbrot(grid$c[i], max_iter, tt)
}

# Aproksymacja powierzchni
area_approx <- mean(grid$in_set) * (4) * (4)
print(area_approx)
