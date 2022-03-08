from datetime import datetime
import time


class Logger:

    def __init__(self, current_folder):
        self.current_folder = current_folder
        self.filename_log = current_folder + "/logs/output_log.txt"
        self.filename_erreur = current_folder + "/logs/output_erreur.txt"
        self.file = open(self.filename_log, "w+")
        self.file.close()
        self.file = open(self.filename_erreur, "w+")
        self.file.close()

    def log_message(self, *args):
        to_write = self.build_message(*args)
        with open(self.filename_log, "a+") as log_file:
            log_file.write(to_write + "\n")
        print(to_write)

    def log_erreur(self, *args):
        to_write = self.build_message(*args)
        with open(self.filename_erreur, "a+") as log_file:
            log_file.write(to_write + "\n")
        # Let's write it anyway in log file
        self.log_message(*args)

    @staticmethod
    def build_message(*args):
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        to_write = "Log [{}] : ".format(dt_string)
        for message in args:
            to_write += str(message) + " "
        return to_write



if __name__ == '__main__':
    logger = Logger("output/")
    logger.log_message("test", "fjg", 9)
    time.sleep(2)
    logger.log_message("test22")
