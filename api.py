from eve import Eve
import pandas as pd

app = Eve()


@app.route('/statistic/<email>')
def statistic(email):
    historico = app.data.driver.db['historico']
    questions = app.data.driver.db['questions']

    questions = pd.DataFrame(questions)
    historico = pd.DataFrame(historico)
    
    query = historico.find(
        "aluno_email":"teste@teste.com"
    )

    data = {
       'aluno' : email,

    }



if __name__ == '__main__':
    app.run()