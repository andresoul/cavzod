from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('index.html')

@app.route('/<data>')
def calcula_signo(data):
  lista_signos = ['Capricornio', 'Aquario', 'Peixes', 'Aries - ',                                            'Touro', 'Gemios', 'Cancer', 'Leao', 'Virgem', 
                    'Libra', 'Escorpiao', 'Sagitario', 'Capricornio']
  lista_cavaleiro = ['SHURA', 'CAMUS', 'AFRODITE OU ALBAFICA', 'MU OU SHIRON', 'ALDEBARAN', 'SAGA OU KANON', 'MANIGOLD', 'AIORIA', 'SHAKA', 'DOHKO', 'MILO', 'SEIYA', 'SHURA']
  lista_datas = [121,219,321,421,521,621,723,823,923,1023,1122,1231,1222]

  periodo = int(data[3:5]+data[:2])
  for i in lista_datas:
    if i > periodo:
      signo = lista_signos[lista_datas.index(i)]
      cavaleiro = lista_cavaleiro[lista_datas.index(i)]
      break
  return jsonify({'signo':signo, 'Seu Cavaleiro e:':cavaleiro})

app.run(host= '0.0.0.0')