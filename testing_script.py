from extras.scripts import Script

class TestScript(Script):
    test_var = StringVar(
        description = "Testing var. Will be echoed back to you at every log level.",
        required = True
    )

    def run(self, data, commit):
        self.log_debug("Congratulations, you can view debug messages")

        self.log_debug(data['test_var'])
        self.log_success(data['test_var'])
        self.log_info(data['test_var'])
        self.log_warning(data['test_var'])
        self.log_failure(data['test_var'])




