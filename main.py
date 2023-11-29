def search_unique(mentors_list):
    mentors_name_list = [i.split(' ')[0] for mentor in mentors_list for i in mentor]

    unique_names = set(mentors_name_list)
    unique_names_sorted = sorted(unique_names)

    return f'Уникальные имена преподавателей: {", ".join(unique_names_sorted)}'


def search_popular(mentors_list):
    mentors_name_list = [i.split(' ')[0] for mentor in mentors_list for i in mentor]

    popular = list(set(((i, mentors_name_list.count(i)) for i in mentors_name_list)))
    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    return (f"{top_3[0][0]}: {top_3[0][1]} раз(а), "
            f"{top_3[1][0]}: {top_3[1][1]} раз(а), "
            f"{top_3[2][0]}: {top_3[2][1]} раз(а)")


def find_super_name(courses_list, mentors_list):
    mentors_name_list = [[course.split(' ')[0] for course in course_list] for course_list in mentors_list]

    for ids, value in enumerate(courses_list):
        for count in range(ids + 1, len(courses_list)):
            courses_par = [value, courses_list[count]]
            intersection_set = set(mentors_name_list[ids]) & set(mentors_name_list[count])
            intersection_sorted = sorted(intersection_set)
            yield f"На курсах '{courses_par[0]}' и '{courses_par[1]}' преподают: {', '.join(intersection_sorted)}"


if __name__ == '__main__':

    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    print(search_unique(mentors))
    print(search_popular(mentors))

    for j in find_super_name(courses, mentors):
        print(j)
