from crewai.tools import tool

@tool
def counter_tool(sentence: str):
    """
    이 함수는 글자수를 정확히 세는 것이다. 문장은 문자열이고 결과값은 숫자열이다
    """

    print("글자수",sentence)
    return len(sentence)