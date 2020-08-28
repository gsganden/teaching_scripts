ROSTER = [
    ("Katharine Alderete", "Kate Alderete"),
    ("Prathyusha Aluri",),
    ("Sandeep	Bansal",),
    ("Diana Buitrago",),
    ("Nishtha Chhabra", "Nish"),
    ("Laura Davis",),
    ("Corey Gibsson",),
    ("Teg Grover",),
    ("Tania Hernandez Baullosa",),
    ("Austin Kiyota",),
    ("Shobha Nikam",),
    ("Suraj Pabba", "Suraj"),
    ("Soo Tan", "Soo Yang Tan"),
    ("Jennet Toyjanova",),
    ("Peter Tran",),
    ("Vasudha Vijay",),
]

SUBMITTED = """
    Jennet Toyjanova
    Tania Hernandez Baullosa
    Suraj
    nish
    Prathyusha Aluri
    Kate Alderete
    Teg Grover
    Diana Buitrago
    Vasudha Vijay
    Soo Yang Tan
    Austin Kiyota
    Peter Tran
"""

ABSENT = """
shobha nikam
corey gibsson
"""


def main():
    submitted = {normalize(name) for name in SUBMITTED.split("\n") if name}
    absent = {normalize(name) for name in ABSENT.split("\n") if name}
    roster = {
        tuple(normalize(name) for name in person_names) for person_names in ROSTER
    }

    print(f"Did not complete:")

    total_count = len(roster) - len(absent)
    completed_count = 0
    for person_names in roster:
        if all(name not in absent for name in person_names):
            if any(name in submitted for name in person_names):
                completed_count += 1
            else:
                print(person_names[0])

    print()
    print(f"{completed_count} out of {total_count}")


def normalize(name):
    return name.lower().strip().replace('\t', ' ').replace('  ', ' ')


if __name__ == "__main__":
    main()
