class Solution(object):
    def interpret(self, command):
        command = command.replace('()','o')
        command = command.replace('(','')
        command = command.replace(')','')
        return command
        