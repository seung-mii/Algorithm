def solution(skill, skill_trees):
    answer = 0
    
    for i, skill_tree in enumerate(skill_trees): 
        for s in skill_tree:
            if s not in skill:
                skill_tree = skill_tree.replace(s, '')
        skill_trees[i] = skill_tree
    
    for skill_tree in skill_trees: 
        if skill_tree == '':
            answer += 1
            continue
            
        idx = 0
        for s in skill_tree:
            if s != skill[idx]:
                break

            idx += 1
            if idx == len(skill_tree):
                answer += 1
    
    return answer