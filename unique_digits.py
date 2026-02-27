import matplotlib.pyplot as plt
import os

def check_repeated_digits(n, include_leading_zeroes=False):
    """Return list of numbers up to n (not inclusive) with no repeated digits.
    if include_leading_zeroes False, 1 counts; if True, 0001 does not."""
    result = []
    for i in range(n):
        clean = True
        if include_leading_zeroes:
            i = '0'*(len(str(n-1))-len(str(i)))+str(i)
        else:
            i = str(i)
        for j in range(len(i)-1):
            for k in range(j+1, len(i)):
                if i[j]==i[k]:
                    clean = False
        if clean:
            result.append(int(i))
    return result

def write_data(result, filename):
    """Write number list to file to skip recalculating."""
    file = open(filename, 'w')
    for line in result:
        file.write(str(line)+'\n')
    file.close()

def read_data(filename, n):
    """Read ints from file, stopping once val>n"""
    numbers = []
    file = open(filename, 'r')
    for line in file:
        val = int(line.strip())
        if val>n:
            break
        numbers.append(val)
    file.close()
    return numbers

def plot_frequency(n, filename=None):
    """Plot frequency of nonrepeated digits for each number up to n (inclusive).
    Read from a file if given, else calculate.
    Calculates upfront and draws from 'master list' instead of
    recalculating with every iteration."""
    frequencies = []
    if not filename:
        numbers = check_repeated_digits(n+1)
    else:
        numbers = read_data(filename, n)
    frequencies = []
    j=0 # pointer into numbers
    for i in range(n+1):
        while j < len(numbers) and numbers[j] <= i:
            j+=1
        frequencies.append(j/(i+1)) # i+1 to ensure 0 counted
    plt.scatter([j for j in range(n+1)], frequencies)
    plt.xlabel('n')
    plt.ylabel("Fraction unique-digit in [0,n]")
    plt.title("Frequency of Unique-Digit Numbers up to n")
    plt.show()

def longest_streaks(numbers):
    """Sort list of numbers by longest streak between each number."""
    vals = {}
    for i in range(len(numbers)-1):
        vals[i] = numbers[i+1]-numbers[i]
    sorted_vals = dict(sorted(vals.items(), key=lambda x: -x[1]))
    result = []
    for val in sorted_vals:
        result.append(str(numbers[val])+'->'+str(numbers[val+1])+': '+
                      str(sorted_vals[val]))
    return result

def save_plot_frequency(n, outpath, filename=None):
    plot_frequency(n, filename)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    plt.savefig(outpath, dpi=300, bbox_inches="tight")
    plt.close()

def main():
    n = int(input())
    result = longest_streaks(check_repeated_digits(n))
    for line in result:
        print(line)

if __name__ == '__main__':
    main()
