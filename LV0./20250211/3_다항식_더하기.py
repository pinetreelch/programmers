# === 3. 다항식 더하기 ===
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

# polynomial	result
# "3x + 7 + x"	"4x + 7"
# "x + x + x"	"3x"

#어제 문제 복기 시도 1

from functools import reduce # lambda와 함께 사용됨

def solution(polynomial):

    polynomial = polynomial.split("+")

    const = 0
    x_sum = 0

    for word in polynomial:
        if "x" in word:
            word = word.replace("x", "1").strip()
             
            # 각 문자(숫자)를 정수 리스트로 변환
            word = list(map(int, list(word)))  
            word = reduce(lambda x, y: x * y, word)

            x_sum += word
            
        else:
            const += int(word)

    return f"{x_sum}x + {const}"

print(solution("3x + 7 + x"))