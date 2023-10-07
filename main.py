from hyperpc import *
from pprint import pprint


def main(hyper: HyperPc) -> None:
    print(f"{COLOR}{LOGO}Created by Qwiii\n")

    for x, value in enumerate(CATEGORIES, 1):
        print(f"{COLOR}{x}::{value}")

    user_input = int(input(f"{COLOR}Select category:: "))

    match user_input:
        case 1:
            hyper.parse_computers_catalog()
            print(f"{COLOR}The result is saved in Catalog.json")
        case 2:
            hyper.parse_optimal_pc()
            print(f"{COLOR}The result is saved in Optimal.json")
        case 3:
            hyper.parse_powerful_pc()
            print(f"{COLOR}The result is saved in Powerful.json")
        case 4:
            hyper.parse_custom_pc()
            print(f"{COLOR}The result is saved in Custom.json")
        case 5:
            pprint(hyper.parse_hardware(url=input(f"{COLOR}Product Link::: ")))
        case _:
            print(f"{COLOR}You entered an incorrect number!")


if __name__ == "__main__":
    main(HyperPc())
