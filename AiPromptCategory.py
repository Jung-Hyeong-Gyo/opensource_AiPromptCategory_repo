def main():
    categories = {}

    while True:
        print("\n==== 프로그램 메뉴 ====")
        print("1. 프롬포트 카테고리 수정 또는 추가")
        print("2. 카테고리 안에 프롬포트 수정 또는 추가")
        print("3. 확인용 전체 카테고리와 프롬포트 같이 출력")
        print("4. 입력용 전체 프롬포트만 출력")
        print("5. 프로그램 종료")
        
        choice = input("선택하세요 (1-5): ").strip()

        if choice == '1':
            manage_categories(categories)
        elif choice == '2':
            manage_prompts(categories)
        elif choice == '3':
            display_all(categories)
        elif choice == '4':
            display_all_prompts(categories)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도해주세요.")

# 1. 프롬포트 카테고리 수정 또는 추가 함수
def manage_categories(categories):
    while True:
        print("\n==== 현재 생성된 카테고리 ====")
        if categories:
            print(', '.join(categories.keys()))
        else:
            print("(현재 생성된 카테고리가 없습니다.)")

        category = input("수정, 추가 또는 삭제할 카테고리 이름을 입력하세요 (b: 뒤로가기): ").strip()
        
        if not category or category.strip() == "":
            print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
            continue

        if category.lower() == 'b':
            print("메뉴로 돌아갑니다.")
            break

        if category in categories:
            print(f"'{category}' 카테고리를 선택했습니다.")
            action = input("이 카테고리의 이름을 수정하려면 새 이름을 입력하고, 삭제하려면 'd'를 입력하세요: ").strip()
            
            if not action or action.strip() == "":
                print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
                continue

            if action.lower() == 'd':
                if category in categories:
                    del categories[category]
                    print(f"'{category}' 카테고리가 삭제되었습니다.")
                else:
                    print(f"'{category}' 카테고리는 이미 삭제되었거나 존재하지 않습니다.")
            elif action and action not in categories:
                categories[action] = categories.pop(category)
                print(f"'{category}'가 '{action}'으로 수정되었습니다.")
            else:
                print("잘못된 입력이거나 이름이 이미 존재합니다.")
        else:
            categories[category] = []
            print(f"'{category}' 카테고리가 추가되었습니다.")

# 2. 카테고리 안에 프롬포트 수정 또는 추가 함수
def manage_prompts(categories):
    if not categories:
        print("카테고리가 존재하지 않습니다. 먼저 카테고리를 추가하세요.")
        return

    while True:
        print("\n==== 현재 생성된 카테고리 ====")
        print(', '.join(categories.keys()))
        
        category = input("프롬포트를 수정하거나 추가할 카테고리를 입력하세요 (b: 뒤로가기): ").strip()

        if not category or category.strip() == "":
            print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
            continue

        if category.lower() == 'b':
            print("\n==== 현재 전체 카테고리 ====")
            print(', '.join(categories.keys()))
            print("메뉴로 돌아갑니다.")
            break

        if category not in categories:
            print(f"'{category}' 카테고리는 존재하지 않습니다.")
            continue

        while True:
            print(f"\n==== '{category}' 카테고리의 프롬포트 ====")
            if categories[category]:
                print(', '.join(categories[category]))
            else:
                print("(현재 프롬포트가 없습니다.)")

            prompt = input("프롬포트를 추가, 수정 또는 삭제할 이름을 입력하세요 (b: 뒤로가기): ").strip()
            if prompt.lower() == 'b':
                break

            if not prompt or prompt.strip() == "":
                print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
                continue

            if prompt in categories[category]:
                action = input("프롬포트를 수정하려면 새 이름을 입력하고, 삭제하려면 'd'를 입력하세요: ").strip()
                if action.lower() == 'd':
                    categories[category].remove(prompt)
                    print(f"'{prompt}' 프롬포트가 삭제되었습니다.")
                elif action and action.strip() != "":
                    categories[category][categories[category].index(prompt)] = action
                    print(f"'{prompt}' 프롬포트가 '{action}'으로 수정되었습니다.")
                else:
                    print("잘못된 입력입니다.")
            else:
                categories[category].append(prompt)
                print(f"'{prompt}' 프롬포트가 추가되었습니다.")

# 3. 전체 카테고리와 프롬포트 출력 함수
def display_all(categories):
    if not categories:
        print("출력할 내용이 없습니다. 카테고리를 먼저 추가하세요.")
        return

    print("\n==== 전체 카테고리 및 프롬포트 ====")
    for category, prompts in categories.items():
        print(f"{category} : {', '.join(prompts) if prompts else '(프롬포트가 없습니다.)'}")

# 4. 전체 프롬포트만 출력 함수
def display_all_prompts(categories):
    if not categories:
        print("출력할 프롬포트가 없습니다. 카테고리를 먼저 추가하세요.")
        return

    print("\n==== 전체 프롬포트 목록 ====")
    all_prompts = [prompt for prompts in categories.values() for prompt in prompts]
    print(', '.join(all_prompts))

if __name__ == "__main__":
    main()
