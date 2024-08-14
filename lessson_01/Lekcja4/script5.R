set.seed(131311)

f <- function(x) 1 / (pi * (1 + x ^ 2))
g <- function(x) 3 / x ^ 2

cauchy <- function(n) {
    samples <- rcauchy(n)
    mean(samples > 3)
}

weighted <- function(n) {
    samples <- (3 / runif(n)) ^ 0.5 # Odwrócona funkcja dystrybuanty dla g(x)
    weights <- f(samples) / g(samples)
    sum(weights) / n
}


n_values <- 1:1000
c_estimates <- sapply(n_values, cauchy)
w_estimates <- sapply(n_values, weighted)

plot(n_values, c_estimates, type = "l", col = "blue",)
lines(n_values, w_estimates, col = "red")
legend("topright", legend = c("Próbkowanie z Cauchy'ego", "Próbkowanie wazone"),
       col = c("blue", "red"), lty = 1)

print(c_estimates[1000])
print(w_estimates[1000])



lambda <- 2
n <- 200
replications <- 200

generate_sample_mean <- function(n, lambda) {
    sample <- rexp(n, rate = lambda)
    return(mean(sample))
}

sample_means <- replicate(replications, generate_sample_mean(n, lambda))

estimated_mean <- mean(sample_means)
estimated_variance <- var(sample_means)

cat("Rzeczywista wartoœæ 1/lamda:", 1 / lambda, "\n")
cat("Œrednia estymatorów:", estimated_mean, "\n")
cat("Wariancja estymatorów:", estimated_variance, "\n")

theoretical_variance <- (1 / lambda) ^ 2 / n
cat("Teoretyczna wariancja estymatora:", theoretical_variance, "\n")



lambda <- 2
n <- 200
r <- 200

generate_Y <- function(n, lambda) {
    1 / mean(rexp(n, rate = lambda))
}

Y <- replicate(r, generate_Y(n, lambda))

obciazenie <- mean(Y) - lambda

var_X <- (1 / lambda) ^ 2 / n
var_Y_delta <- (lambda ^ 4) * var_X

mse <- mean((Y - lambda) ^ 2)

cat("Obci¹¿enie:", obciazenie, "\n")
cat("Wariancja (metoda delta):", var_Y_delta, "\n")
cat("MSE:", mse, "\n")
cat("Kwadrat obci¹¿enia:", obciazenie ^ 2, "\n")
cat("Stosunek kwadratu obci¹¿enia do MSE:", obciazenie ^ 2 / mse, "\n")