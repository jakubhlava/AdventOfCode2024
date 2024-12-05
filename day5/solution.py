with open("input.txt", "r") as f:
    textrules, textupdates = [p.split("\n") for p in f.read().strip().split("\n\n")]

rules = [[int(x) for x in r.split("|")] for r in textrules]
updates = [list(map(int, u.split(","))) for u in textupdates]

def is_incorrect(update):
    for i, page in enumerate(update):
        if is_incorrect_step(i, page, update):
            return True
    return False

def is_incorrect_step(i, page, update):
    active_rules = [r for r in rules if r[0] == page]
    violated_rules = [r[1] in update[:i] for r in active_rules]

    return any(violated_rules)

correct_updates = []
incorrect_updates = []
for update in updates:
    if is_incorrect(update):
        incorrect_updates.append(update)
    else:
        correct_updates.append(update)

print("Part 1:", sum([x[len(x) // 2] for x in correct_updates]))

for update in incorrect_updates:
    while is_incorrect(update):
        for i, page in enumerate(update):
            active_rules = [r for r in rules if r[0] == page]
            violated_rules = [r for r in active_rules if r[1] in update[:i]]
            if len(violated_rules) > 0:
                applied_rule = violated_rules[0]
                update.remove(applied_rule[0])
                update.insert(update.index(applied_rule[1]), applied_rule[0])

print("Part 2:", sum([x[len(x) // 2] for x in incorrect_updates]))
