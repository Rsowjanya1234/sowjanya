import src.calculations

@pytest.mark.parameterize('num1', 'num2','result',[ (10,20,30), (20,30,50) ,(4,5,9)])
def test_add(num1, num2,result):
    assret.src.calculations.add(num1,num2) == result

