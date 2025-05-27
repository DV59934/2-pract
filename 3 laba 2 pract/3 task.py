class Calculation:
    def __init__(self, calculationLine):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, calculationLine):
        self.calculationLine = calculationLine

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine = self.calculationLine + symbol

    def GetCalculationLine(self):
        return self.calculationLine

    def GetLastSymbol(self):
        return self.calculationLine[-1]

    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]

text = Calculation("Hello world")
text.SetLastSymbolCalculationLine("!")
print(f"Прибавление символа: {text.GetCalculationLine()}")
text.DeleteLastSymbol()
print(f"Значение свойств: {text.GetCalculationLine()}")
text.DeleteLastSymbol()
print(f"Удаление последнего элемента строки: {text.GetCalculationLine()}")
