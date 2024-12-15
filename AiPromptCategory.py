def main():
    # 메인 함수: 프로그램의 시작점이며 사용자에게 메뉴를 표시하고 선택에 따라 기능을 실행합니다.
    categories = {}  # 카테고리를 저장하는 딕셔너리

    while True:
        # 프로그램 메뉴 출력
        print("\n==== 프로그램 메뉴 ====")
        print("1. 프롬포트 카테고리 수정 또는 추가")
        print("2. 카테고리 안에 프롬포트 수정 또는 추가")
        print("3. 확인용 전체 카테고리와 프롬포트 같이 출력")
        print("4. 입력용 전체 프롬포트만 출력")
        print("5. 프로그램 종료")
        
        choice = input("선택하세요 (1-5): ").strip()  # 사용자 입력 받기

        # 사용자의 선택에 따라 각 기능을 실행
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
            break  # 프로그램 종료
        else:
            print("올바른 선택이 아닙니다. 다시 시도해주세요.")

# 1. 프롬포트 카테고리 수정 또는 추가 함수
def manage_categories(categories):
    # 카테고리를 추가, 수정, 삭제하는 기능을 제공하는 함수
    while True:
        print("\n==== 현재 생성된 카테고리 ====")
        if categories:
            print(', '.join(categories.keys()))  # 현재 존재하는 카테고리 출력
        else:
            print("(현재 생성된 카테고리가 없습니다.)")

        category = input("수정, 추가 또는 삭제할 카테고리 이름을 입력하세요 (b: 뒤로가기): ").strip()
        
        # 입력 검증: 빈칸 또는 공백 입력 방지
        if not category or category.strip() == "":
            print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
            continue

        # 뒤로 가기 처리
        if category.lower() == 'b':
            print("메뉴로 돌아갑니다.")
            break

        # 카테고리가 이미 존재하는 경우 수정 또는 삭제
        if category in categories:
            print(f"'{category}' 카테고리를 선택했습니다.")
            action = input("이 카테고리의 이름을 수정하려면 새 이름을 입력하고, 삭제하려면 'd'를 입력하세요: ").strip()
            
            # 입력 검증
            if not action or action.strip() == "":
                print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
                continue

            # 카테고리 삭제 처리
            if action.lower() == 'd':
                del categories[category]
                print(f"'{category}' 카테고리가 삭제되었습니다.")
            # 카테고리 이름 수정 처리
            elif action and action not in categories:
                categories[action] = categories.pop(category)
                print(f"'{category}'가 '{action}'으로 수정되었습니다.")
            else:
                print("잘못된 입력이거나 이름이 이미 존재합니다.")
        else:
            # 새로운 카테고리 추가
            categories[category] = []
            print(f"'{category}' 카테고리가 추가되었습니다.")

# 2. 카테고리 안에 프롬포트 수정 또는 추가 함수
def manage_prompts(categories):
    # 카테고리 내 프롬포트를 추가, 수정, 삭제하는 기능을 제공하는 함수
    if not categories:
        print("카테고리가 존재하지 않습니다. 먼저 카테고리를 추가하세요.")
        return

    while True:
        print("\n==== 현재 생성된 카테고리 ====")
        print(', '.join(categories.keys()))  # 카테고리 목록 출력
        
        category = input("프롬포트를 수정하거나 추가할 카테고리를 입력하세요 (b: 뒤로가기): ").strip()

        # 입력 검증
        if not category or category.strip() == "":
            print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
            continue

        # 뒤로 가기 처리
        if category.lower() == 'b':
            print("\n==== 현재 전체 카테고리 ====")
            print(', '.join(categories.keys()))
            print("메뉴로 돌아갑니다.")
            break

        if category not in categories:  # 존재하지 않는 카테고리 처리
            print(f"'{category}' 카테고리는 존재하지 않습니다.")
            continue

        while True:
            print(f"\n==== '{category}' 카테고리의 프롬포트 ====")
            if categories[category]:
                print(', '.join(categories[category]))  # 프롬포트 출력
            else:
                print("(현재 프롬포트가 없습니다.)")

            prompt = input("프롬포트를 추가, 수정 또는 삭제할 이름을 입력하세요 (b: 뒤로가기): ").strip()
            
            # 뒤로 가기 처리
            if prompt.lower() == 'b':
                break

            # 입력 검증
            if not prompt or prompt.strip() == "":
                print("잘못된 입력입니다. 빈칸 또는 공백은 허용되지 않습니다.")
                continue

            # 프롬포트 수정 또는 삭제 처리
            if prompt in categories[category]:
                action = input("프롬포트를 수정하려면 새 이름을 입력하고, 삭제하려면 'd'를 입력하세요: ").strip()
                if action.lower() == 'd':
                    categories[category].remove(prompt)  # 프롬포트 삭제
                    print(f"'{prompt}' 프롬포트가 삭제되었습니다.")
                elif action and action.strip() != "":
                    categories[category][categories[category].index(prompt)] = action  # 프롬포트 수정
                    print(f"'{prompt}' 프롬포트가 '{action}'으로 수정되었습니다.")
                else:
                    print("잘못된 입력입니다.")
            else:
                # 새로운 프롬포트 추가
                categories[category].append(prompt)
                print(f"'{prompt}' 프롬포트가 추가되었습니다.")

# 3. 전체 카테고리와 프롬포트 출력 함수
def display_all(categories):
    # 모든 카테고리와 각 카테고리에 속한 프롬포트를 출력하는 함수
    if not categories:
        print("출력할 내용이 없습니다. 카테고리를 먼저 추가하세요.")
        return

    print("\n==== 전체 카테고리 및 프롬포트 ====")
    for category, prompts in categories.items():
        print(f"{category} : {', '.join(prompts) if prompts else '(프롬포트가 없습니다.)'}")

# 4. 전체 프롬포트만 출력 함수
def display_all_prompts(categories):
    # 모든 프롬포트만 출력하는 함수
    if not categories:
        print("출력할 프롬포트가 없습니다. 카테고리를 먼저 추가하세요.")
        return

    print("\n==== 전체 프롬포트 목록 ====")
    all_prompts = [prompt for prompts in categories.values() for prompt in prompts]  # 모든 프롬포트 수집
    print(', '.join(all_prompts))

if __name__ == "__main__":
    main()
