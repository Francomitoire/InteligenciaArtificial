import sys
import math
import wx





__license__ = "GPL"




class Calculator(object):
    #tu mama

    def __init__(self):
        self.operators = {"+": self.Sum,
                          "-": self.Rest,
                          "*": self.Mult,
                          "/": self.Div,
                          u"+-": self.Negative,
                          u"x*": self.Square,
                          u"1/x": self.OneInX,
                          u"Raiz": self.Squareroot,
                          u"%": self.Percent,
                          u"C": self.Clear
                          }
        self.arith_operators = {"+": self.Sum,
                                "-": self.Rest,
                                "*": self.Mult,
                                "/": self.Div
                                }
        self.espec_operators = {u"+-": self.Negative,
                                u"x*": self.Square,
                                u"1/x": self.OneInX,
                                u"Raiz": self.Squareroot,
                                u"%": self.Percent,
                                u"C": self.Clear}

        self.expression = []
        self.expression_string = u""
        self.result = 0.0

    def IsNumber(self, string):
        try:
            float(string)
        except ValueError:
            return False
        return True

    def Sum(self, num_1, num_2):
        """
        Sumar: num_1 + num_2
        """
        return num_1 + num_2

    def Rest(self, num_1, num_2):
        """
        Restar: num_1 - num_2
        """
        return num_1 - num_2

    def Mult(self, num_1, num_2):
        """
        Multiplicar: num_1 * num_2
        """
        return num_1 * num_2

    def Div(self, num_1, num_2):
        """
        Dividir: num_1 / num_2
        """
        return num_1 / num_2

    def Negative(self, num):
        """
        Convirte el numero positivo en negativo y viceversa.
        """
        return -num

    def Square(self, num):
        """
        Retorna el cuadrado del numero indicado.
        """
        return num * num

    def Squareroot(self, num):
        """
        Retorna la raiz cuadrada del numero indicado.
        Para tal fin utilizamos la funcion sqrt del modulo math.
        """
        return math.sqrt(num)

    def OneInX(self, num):
        """
        Dividimos el numero 1 entre el numero indicado.
        """
        return 1.0 / num

    def Percent(self, num, percent=100):
        """
        Calculamos el porcentaje indicado al numero.
        """
        return (num / 100.0) * percent

    def Clear(self):
        """
        Limpia los datos introduccidos.
        """
        self.expression = []

    def Calculate(self, num_1, num_2, operator):
        """
        Calcula num_1 y num_2 segun el operador indicado.
        """
        expression = "%s %s %s" % (num_1, operator, num_2)
        exec "out = %s" % expression
        return out

    def Reduce(self, choice):
        """
        Resuelve las operaciones de lista hasta
        que no quede mas elementos. Retorna el resultado.
        """
        out = 0.0
        result = float(choice[0])
        for n in range(0, len(choice), 2):
            number_1 = result

            try:
                operator = choice[n + 1]
            except IndexError:
                break

            try:
                number_2 = float(choice[n + 2])
            except (IndexError, ValueError):
                number_2 = number_1

            try:
                if choice[n + 3] == "%":
                    number_2 = self.Percent(num_1, num2)
            except IndexError:
                pass

            # si es un operador especial
            if operator in self.espec_operators.keys():
                result = self.operators[operator](number_1)
            else:
                result = self.Calculate(number_1, number_2, operator)
            out += result
        return out

    def Solve(self):
        """
        Resuelve la expression.
        """
        self.expression_string = unicode.join(u" ", self.expression)
        try:
            exec ("self.result = %s" % self.expression_string)
        except SyntaxError as e:
            print(e)
        return self.result


"""Interfaz"""

class DlgCalculator(wx.Dialog, Calculator):
    """Interfaz grafica de una calculadora simple.
    """

    def __init__(self, parent, *args, **kwargs):
        wx.Dialog.__init__(self, parent, *args, **kwargs)
        Calculator.__init__(self)
        # definimos los controles
        self.textctrl_1 = wx.TextCtrl(self, -1, style=wx.TE_READONLY | wx.NO_BORDER | wx.TE_RIGHT)
        self.textctrl_2 = wx.TextCtrl(self, -1, style=wx.TE_READONLY | wx.NO_BORDER | wx.TE_RIGHT)
        self.button_0 = wx.Button(self, 0, u"0")
        self.button_1 = wx.Button(self, 1, u"1")
        self.button_2 = wx.Button(self, 2, u"2")
        self.button_3 = wx.Button(self, 3, u"3")
        self.button_4 = wx.Button(self, 4, u"4")
        self.button_5 = wx.Button(self, 5, u"5")
        self.button_6 = wx.Button(self, 6, u"6")
        self.button_7 = wx.Button(self, 7, u"7")
        self.button_8 = wx.Button(self, 8, u"8")
        self.button_9 = wx.Button(self, 9, u"9")
        self.button_10 = wx.Button(self, 10, u".")
        self.button_11 = wx.Button(self, 11, u"+")
        self.button_12 = wx.Button(self, 12, u"-")
        self.button_13 = wx.Button(self, 13, u"x")
        self.button_14 = wx.Button(self, 14, u"%")
        self.button_15 = wx.Button(self, 15, u"+-")
        self.button_16 = wx.Button(self, 16, u"x*")
        self.button_17 = wx.Button(self, 17, u"1/x")
        self.button_18 = wx.Button(self, 18, u"Raiz")
        self.button_19 = wx.Button(self, 19, u"%")
        self.button_20 = wx.Button(self, 20, u"C")
        self.button_21 = wx.Button(self, 21, u"=")
        # variables
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.expression = []
        self.expression_string = u""
        self.result = 0.0

        self.__do_layout()
        self.__set_prop()
        self.__set_event()

    def __do_layout(self):
        """
        Establecemos los sizer y
        organizamos los controles en ellos.
        """
        s1 = wx.BoxSizer(wx.VERTICAL)

        s2 = wx.BoxSizer(wx.VERTICAL)
        s2.Add(self.textctrl_1, 0, wx.EXPAND | wx.DOWN, 5)
        s2.Add(self.textctrl_2, 1, wx.EXPAND)
        s1.Add(s2, 1, wx.EXPAND | wx.ALL, 5)
        s1.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        s3 = wx.GridSizer(6, 4, 0, 0)  # 6 filas, 4 columnas
        # botones fila 1
        s3.Add(self.button_16, 0, wx.EXPAND)
        s3.Add(self.button_20, 0, wx.EXPAND)
        s3.AddSpacer(1)
        s3.AddSpacer(1)
        # botones fila 2
        s3.Add(self.button_19, 0, wx.EXPAND)
        s3.Add(self.button_18, 0, wx.EXPAND)
        s3.Add(self.button_17, 0, wx.EXPAND)
        s3.Add(self.button_14, 0, wx.EXPAND)
        # botones fila 3
        s3.Add(self.button_7, 0, wx.EXPAND)
        s3.Add(self.button_8, 0, wx.EXPAND)
        s3.Add(self.button_9, 0, wx.EXPAND)
        s3.Add(self.button_13, 0, wx.EXPAND)
        # botones fila 4
        s3.Add(self.button_4, 0, wx.EXPAND)
        s3.Add(self.button_5, 0, wx.EXPAND)
        s3.Add(self.button_6, 0, wx.EXPAND)
        s3.Add(self.button_12, 0, wx.EXPAND)
        # botones fila 5
        s3.Add(self.button_1, 0, wx.EXPAND)
        s3.Add(self.button_2, 0, wx.EXPAND)
        s3.Add(self.button_3, 0, wx.EXPAND)
        s3.Add(self.button_11, 0, wx.EXPAND)
        # botones fila 6
        s3.Add(self.button_15, 0, wx.EXPAND)
        s3.Add(self.button_0, 0, wx.EXPAND)
        s3.Add(self.button_10, 0, wx.EXPAND)
        s3.Add(self.button_21, 0, wx.EXPAND)

        s1.Add(s3, 3, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(s1)
        s1.Fit(self)
        self.Layout()

    def __set_prop(self):
        """
        Establecemos algunas propiedades extras a los controles.
        """
        self.SetSize((400, 400))
        self.textctrl_2.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        # color y fuente de los botones
        for id in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            button = self.FindWindowById(id)
            button.SetBackgroundColour(wx.Colour(255, 255, 200))
            button.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        for id in (11, 12, 13, 14):
            button = self.FindWindowById(id)
            button.SetBackgroundColour(wx.Colour(200, 255, 200))
            button.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        for id in (15, 16, 17, 18, 19):
            button = self.FindWindowById(id)
            button.SetBackgroundColour(wx.Colour(200, 200, 255))
            button.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        for id in (20,):
            button = self.FindWindowById(id)
            button.SetBackgroundColour(wx.Colour(255, 200, 200))
            button.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

    def __set_event(self):
        """
        Establecemos los eventos a los controles.
        """
        for bid in range(22):
            self.Bind(wx.EVT_BUTTON, self.OnClick, id=bid)

    def OnClick(self, event):
        """
        Al presionar uno de los botones.
        """
        character = event.GetEventObject().GetLabel()
        if character == u"x":
            character = u"*"
        elif character == u"%":
            character = u"/"

        if not self.expression:
            if character in self.numbers:
                self.expression.append(character)

        elif character == u"=":
            self.Solve()

        elif character == u"C":
            self.expression = []
            self.result = 0.0

        elif self.expression[-1] in self.numbers:
            if character == u"+-":
                self.expression[-1] = u"%s" % -float(self.expression[-1])

            elif character == u"x*":
                self.expression[-1] = u"%s" % (float(self.expression[-1]) * float(self.expression[-1]))

            elif character == u"1/x":
                self.expression[-1] = u"%s" % (1 / float(self.expression[-1]))

            elif character == u"Raiz":
                self.expression[-1] = u"%s" % math.sqrt(float(self.expression[-1]))

            elif character == u"%":
                n1 = float(self.expression[-3])
                self.expression[-1] = u"%s" % ((n1 / 100) * float(self.expression[-1]))

            elif character in ("*", "/", "-", "+"):
                self.expression.append(character)
                self.Solve()

            elif character in self.numbers:
                self.expression[-1] += character


        else:
            if character in self.numbers:
                self.expression.append(character)

            elif character in ("*", "/", "-", "+"):
                self.expression[-1] = character

        self.expression_string = unicode.join(u" ", self.expression)
        self.textctrl_1.SetValue(self.expression_string)
        self.textctrl_2.SetValue(str(self.result))
        event.Skip()

    def Solve(self):
        try:
            exec ("self.result = %s" % self.expression_string)
        except SyntaxError:
            pass
        return self.result


def main(args):
    app = wx.App(0)
    dlg = DlgCalculator(None, id=-1, title=u"Calculadora")
    dlg.Show()
    app.MainLoop()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))


