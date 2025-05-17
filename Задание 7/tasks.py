def factorial_mod_p(n, p):
    """
    Вычисление N! mod P, где P — простое число, за O(p log_p N).
    """
    def count_p_in_factorial(n, p):
        """
        Подсчет кратности числа P в разложении факториала N!.
        """
        count = 0
        power = p
        while power <= n:
            count += n // power
            power *= p
        return count

    def factorial_mod(n, p):
        """
        Вычисление факториала N! по модулю P.
        """
        result = 1
        for i in range(1, n + 1):
            if i % p != 0:  # Пропускаем числа, кратные P
                result = (result * i) % p
        return result

    # Шаг 1: Подсчет кратности P в N!
    e = count_p_in_factorial(n, p)

    # Шаг 2: Если e > 0, то N! mod P = 0
    if e > 0:
        return 0

    # Шаг 3: Вычисляем факториал по модулю P
    result = 1
    while n > 0:
        result = (result * factorial_mod(n % p, p)) % p
        n //= p

    return result

# Пример использования
if __name__ == "__main__":
    N = 10
    P = 7
    print(f"{N}! mod {P} = {factorial_mod_p(N, P)}")