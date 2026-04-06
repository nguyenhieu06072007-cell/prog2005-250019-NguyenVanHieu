students = {
    "An": 8,
    "Binh": 7,
    "Cuong": 9
}

def average_score(d):
    return sum(d.values()) / len(d)

print("Điểm TB:", average_score(students))