# Instalacja i wczytanie pakietu ks
# install.packages("ks")
library(ks)

# Ustawienia
alpha <- 0.05
n <- 100 # rozmiar próby
num_simulations <- 10000 # liczba symulacji
beta_params <- list(c(2, 3), c(4, 2), c(3, 5), c(5, 3)) # wybrane parametry rozk³adu beta

# Funkcja do symulacji mocy testu KS
simulate_power_ks <- function(n, alpha, num_simulations, shape1, shape2) {
    reject_count <- 0

    for (i in 1:num_simulations) {
        sample <- rbeta(n, shape1, shape2)
        ks_stat <- ks.test(sample, "pbeta", shape1, shape2)$statistic

        # Próg krytyczny dla rozmiaru próby n i poziomu istotnoœci alpha
        critical_value <- ks.test.beta(n, alpha, shape1, shape2)$quantile

        if (ks_stat > critical_value) {
            reject_count <- reject_count + 1
        }
    }

    power <- reject_count / num_simulations
    return(power)
}

# Obliczanie mocy testu KS dla ró¿nych rozk³adów beta
powers <- sapply(beta_params, function(params) {
    simulate_power_ks(n, alpha, num_simulations, params[1], params[2])
})

# Wyœwietlenie wyników
powers