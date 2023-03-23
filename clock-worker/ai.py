import moment

class AI:
    def get_tomorrow_day(self):
        tomorrow = self.get_tomorrow().add(days=1)
        return 'According to AI, tomorrow is ' + tomorrow.format("dddd")

    def get_now(self):
        return moment.now()