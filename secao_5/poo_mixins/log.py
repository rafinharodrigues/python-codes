# Abstração

class Log():

    def log(self, msg):
        return NotImplementedError("Implemente o método log")
    
class LogFileMixin(Log):

    def log(self, msg):
        print(msg)
        
    


if __name__ == '__main__':

    log = LogFileMixin()
    log.log("Olá")