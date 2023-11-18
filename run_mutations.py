import pytest
from Polynomial import Polynomial  # Import the original Polynomial class
from MutationOperators import MutationOperators  # Import the mutation operators
from PolyTest import test_init, test_str, test_add, test_sub, test_mul, \
    test_first_degree_polynomial, test_second_degree_polynomial, test_third_degree_polynomial

def main():
    # Original Polynomial
    original_poly = Polynomial([3, 0, 2])

    # Creating mutants using mutation operators
    mutant_coefficient = MutationOperators.coefficient_mutation(Polynomial([3, 0, 2]))
    mutant_arithmetic = MutationOperators.arithmetic_operation_mutation(Polynomial([3, 0, 2]))
    mutant_boundary = MutationOperators.boundary_mutation(Polynomial([3, 0, 2]))
    mutant_conditional = MutationOperators.conditional_statement_mutation(Polynomial([3, 0, 2]))
    mutant_redundant = MutationOperators.redundant_code_injection(Polynomial([3, 0, 2]))

    # List of test functions without mutants
    test_functions_without_mutants = [test_init, test_str, test_add, test_sub, test_mul,
                                      test_first_degree_polynomial, test_second_degree_polynomial,
                                      test_third_degree_polynomial]

    # List of test functions with mutants
    test_functions_with_mutants = [test_init, test_str, test_add, test_sub, test_mul,
                                    test_first_degree_polynomial, test_second_degree_polynomial,
                                    test_third_degree_polynomial]

    # Running tests on original Polynomial
    for test_func in test_functions_without_mutants:
        test_func()

    # Running tests on mutants
    for test_func in test_functions_with_mutants:
        test_func()

if __name__ == "__main__":
    main()
