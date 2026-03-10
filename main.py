from services.verifier import verify_claim


if __name__ == "__main__":

    claim = input("Enter a claim to verify: ")

    result = verify_claim(claim)

    print("\nResult:\n")
    print(result)