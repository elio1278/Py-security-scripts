def rail_fence_decrypt(ciphertext, num_rails):
    matrix = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]
    
    dir_down = None
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        matrix[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*' and index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        if matrix[row][col] != '\n':
            result.append(matrix[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)


if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    num_rails = int(input("Enter the number of rails: "))
    plaintext = rail_fence_decrypt(ciphertext, num_rails)
    print("Decrypted text:", plaintext)
