import log

log2 = log.Log()

print(log2.log("Executando na main"))

log3 = log.LogFileMixin()
log3.log("teste")