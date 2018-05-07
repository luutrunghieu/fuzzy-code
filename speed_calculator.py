import fuzzy_rule_base.read_rule as read_rule
import fuzzification.fuzzy_dependency as fuzzy_dependency
def calculate_speed(impediment,distance,light_status):
    if impediment:
        impediment_rules = read_rule.read_impediment_rule()
        distance_dependencies = fuzzy_dependency.cal_distance_dependencies(distance)
        numerator = 0
        denominator = 0
        for rule in impediment_rules:
            for dependency in distance_dependencies:
                if rule[0] == dependency[0]:
                    if rule[1] == 'Stop':
                        numerator = numerator + dependency[1]*0
                    elif rule[1] == 'Medium':
                        numerator = numerator + dependency[1]*0.5
                    elif rule[1] == 'Fast':
                        numerator = numerator + dependency[1]*1.5
                    denominator = denominator + dependency[1]
        return (numerator/denominator)

    else :
        light_rules = read_rule.read_light_rule()
        distance_dependencies = fuzzy_dependency.cal_distance_dependencies(distance)
        light_dependencies = fuzzy_dependency.cal_light_dependencies(light_status)
        numerator = 0
        denominator = 0
        for rule in light_rules:
            for distance_dependency in distance_dependencies:
                for light_dependency in light_dependencies:
                    if rule[0] == distance_dependency[0] and rule[1] == light_dependency[0]:
                        if rule[2] == 'Stop':
                            numerator = numerator + distance_dependency[1]*light_dependency[1]*0
                        if rule[2] == 'Slow':
                            numerator = numerator + distance_dependency[1]*light_dependency[1]*0.5
                        elif rule[2] == 'Medium':
                            numerator = numerator + distance_dependency[1]*light_dependency[1]*1
                        elif rule[2] == 'Fast':
                            numerator = numerator + distance_dependency[1]*light_dependency[1]*1.5
                        denominator = denominator + distance_dependency[1]*light_dependency[1]
        return (numerator/denominator)

# Goi function calculate_speed de tinh speed
# Cac tham so 
#   arg[0]: la vat can hay la den. Neu la vat can thi arg[0] = 1, neu la den thi arg[0] = 0
#   arg[1]: khoang cach den vat can hoac den den
#   arg[2]: la trang thai cua den gom thoi gian va trang thai (xanh la 1, do la 2)

# Example: 
# arg[0] = 0 => la den
# arg[1] = 120 => khoang cach la 120
# arg[2] = [5,2] => la den do va thoi gian = 5s
print("speed: {0}".format(calculate_speed(0,120,[5,2])))