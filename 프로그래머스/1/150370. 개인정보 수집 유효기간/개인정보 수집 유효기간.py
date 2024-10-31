def solution(today, terms, privacies):
    answer = []
    term_dict = {}

    cur_year, cur_month, cur_day = map(int, today.split('.'))
    
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value)

    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        y, m, d = map(int, date.split('.'))

        m += term_dict[term_type]
        
        if m > 12:
            y += (m - 1) // 12
            m = (m - 1) % 12 + 1

        if (y < cur_year) or (y == cur_year and m < cur_month) or (y == cur_year and m == cur_month and d <= cur_day):
            answer.append(i + 1)

    return answer