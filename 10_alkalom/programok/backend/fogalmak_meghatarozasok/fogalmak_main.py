from DefinitionDict import DefinitionDict
from QuestionHandler import QuestionHandler
from Game import Game


def main():
    fogalmak = [
        'majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized',
        'kilenced', 'robot', 'szügyhám', 'vetésforgó', 'ugar', 'lovag'
    ]
    meghatarozasok = [
        'Egy-egy nagybirtok vagy valamely részének igazgatási központja.',
        'Aki örökletes használatra megkapja a földet.',
        'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.',
        'Kiváltságos réteg.',
        'Egyházi adó.',
        'Földesúrnak beszolgáltatott adó.',
        'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.',
        'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.',
        'A termőföld használata évszakonként más és más.',
        'Művelés alá nem vont terület.',
        'Vagyonos katonai szolgálattevő lóval, páncéllal.'
    ]

    dicitonary = DefinitionDict(fogalmak, meghatarozasok)
    question_handler = QuestionHandler(dicitonary)

    while True:
        game = Game(question_handler)
        game.play()
        game.display_result()

        if not game.ask_for_new_game():
            print("Köszi, viszlát!")
            break


main()
