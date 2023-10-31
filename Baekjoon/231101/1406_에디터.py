import sys
input = sys.stdin.readline

class editor(object):
    def __init__(self, s:str) -> None:
        self.left = list(s)
        self.right = list()
    
    def command_input(self, command:str):
        command = command.split()
        if command[0] == 'L':
            self.command_L()
        elif command[0] == 'D':
            self.command_D()
        elif command[0] == 'B':
            self.command_B()
        elif command[0] == 'P':
            self.command_P(command[1])

    def command_L(self):
        # 커서가 문장의 맨 앞이면 무시됨
        try:
            self.right.append(self.left.pop())
        except:
            pass

    def command_D(self):
        # 커서가 문장의 맨 뒤이면 무시됨
        try:
            self.left.append(self.right.pop())
        except:
            pass
    
    def command_B(self):
        # 커서가 문장의 맨 앞이면 무시됨
        try:
            self.left.pop()
        except:
            pass  
    
    def command_P(self, alp:str):
        self.left.append(alp)
    
        
editor = editor(input().strip())
num = int(input())

for i in range(num):
    command = input().strip()
    editor.command_input(command)

print(''.join(editor.left) + ''.join(editor.right[::-1]))
