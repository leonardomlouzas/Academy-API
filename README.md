# **Kenzie-Fit**

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus risus eget ornare fermentum. Vestibulum odio orci, tincidunt sit amet malesuada eget, porttitor nec felis. Ut vestibulum ullamcorper convallis.

> <p>BASE URL: <a href="https://academy-api-kenzie.herokuapp.com/">AQUI</a></p>
> <p>Front-End: <a href="https://github.com/thdias00/kenzie-fit">AQUI</a></p>

---

## **Documentação**

- ### **Personais**

<details>
  <summary>POST <code>/personal/signup</code></summary>
<p>Cadastra um novo personal no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Augusto Pereira",
  "email": "Augusto@email.com",
  "cpf": "333.333.333-33",
  "senha": "*aA123456"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 2,
  "nome": "Augusto Pereira",
  "email": "Augusto@email.com",
  "cpf": "333.333.333-33",
  "alunos": []
}
```

</details>

<details>
  <summary>GET <code>/personal</code></summary>
<p>Retorna uma lista contendo todos os personais cadastrados no banco de dados.</p>
Corpo da requisição:

```
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "personal": [
    {
      "id": 1,
      "nome": "José Alves",
      "email": "jose1@email.com",
      "cpf": "333.333.333-32",
      "alunos": []
    },
    {
      "id": 2,
      "nome": "Augusto Pereira",
      "email": "Augusto@email.com",
      "cpf": "333.333.333-33",
      "alunos": []
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/personal/profile</code></summary>
<p>Retorna as informações do personal indicado no token.</p>
Corpo da requisição:

```
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "id": 2,
  "nome": "Augusto Pereira",
  "email": "Augusto@email.com",
  "cpf": "333.333.333-33",
  "alunos": []
}
```

</details>

<details>
  <summary>POST <code>/personal/signin</code></summary>
<p>Realiza o login de um personal já cadastrado no banco de dados.</p>
Corpo da requisição:

```json
{
  "email": "jose1@email.com", //Obrigatório
  "senha": "Aa*123" //Obrigatório
}
```

Corpo da resposta `200 OK`:

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

</details>

<details>
  <summary>PATCH <code>/personal</code></summary>
<p>Atualiza as informações de um personal já cadastrado no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Augusto Pereira Silva"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 2,
  "nome": "Augusto Pereira Silva",
  "email": "Augusto@email.com",
  "cpf": "333.333.333-33",
  "alunos": []
}
```

</details>

<details>
  <summary>DELETE <code>/personal</code></summary>
<p>Exclui um personal do banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `204 NO CONTENT`:

```json
Não há corpo
```

</details>

- ### **Alunos**

<details>
  <summary>POST <code>/students</code></summary>
<p>Cadastra um novo aluno no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Antonio Ruiz",
  "telefone": "(99)99999-9999",
  "email": "antonio@email.com",
  "peso": 80,
  "altura": 1.75
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "Antonio Ruiz",
  "telefone": "(99)99999-9999",
  "email": "antonio@email.com",
  "peso": 80,
  "altura": 1.75,
  "id": 1,
  "imc": 26.1,
  "personal": {
    "id": 1,
    "nome": "José Alvez",
    "cpf": "333.333.333-33"
  }
}
```

</details>

<details>
  <summary>GET <code>/students</code></summary>
<p>Retorna uma lista contendo todos os alunos cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
    "alunos": [
        {
        "id": 1,
        "nome": "Antonio Luiz",
        "telefone": "(99)99999-9999",
        "email": "antonio@email.com",
        "peso": 80,
        "altura": 1.75,
        "imc": 26.1,
        "treinos": [
            {"id": 1,
            "nome": "A",
            "personal": {
                "nome": "José Alvez",
                "email": "jose@alves.com",
                "cpf": "333.333.333-33"
            },
            "dia": "Segunda-Feira",
            "exercicios": [
                {
                    "id": 1,
                    "nome": "Supino Reto",
                    "execução": {
                        "id": 1,
                        "series": 3,
                        "repetições": 10,
                        "carga": "10kg de cada lado"
                },
                "aparelho": {
                    "id": 1,
                    "nome": "Máquina Supino",
                    "código": 1
                }
                },
                {
                    "id": 2,
                    "nome": "Pack Deck",
                    "execução": {
                        "id": 2,
                        "series": 4,
                        "repetições": 12,
                        "carga": "40kg"
                    },
                    {"aparelho": {
                        "id": 2,
                        "nome": "Pack Deck",
                        "código": 5
                    }
                    }
                }
            ]
            }
        ]
        }
    ]
}
```

</details>

<details>
  <summary>GET <code>/students/:id</code></summary>
<p>Retorna as informações do aluno indicado na url.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
    "id": 1,
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 1.75,
    "imc": 26.1,
    "treinos": [
        {"id": 1,
        "nome": "A",
        "personal": {
            "nome": "José Alvez",
            "email": "jose@alves.com",
            "cpf": "333.333.333-33"
        },
        "dia": "Segunda-Feira",
        "exercicios": [
            {
                "id": 1,
                "nome": "Supino Reto",
                "execução": {
                    "id": 1,
                    "series": 3,
                    "repetições": 10,
                    "carga": "10kg de cada lado"
            },
            "aparelho": {
                "id": 1,
                "nome": "Máquina Supino",
                "código": 1
            }
            },
            {
                "id": 2,
                "nome": "Pack Deck",
                "execução": {
                    "id": 2,
                    "series": 4,
                    "repetições": 12,
                    "carga": "40kg"
                },
                {"aparelho": {
                    "id": 2,
                    "nome": "Pack Deck",
                    "código": 5
                }
                }
            }
        ]
        }
    ]
}
```

</details>

<details>
  <summary>PATCH <code>/students</code></summary>
<p>Atualiza as informações de um aluno no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Antonio Luiz"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "Antonio Luiz",
  "telefone": "(99)99999-9999",
  "email": "antonio@email.com",
  "peso": 80,
  "altura": 1.75,
  "imc": 26.1
}
```

</details>

<details>
  <summary>DELETE <code>/students/:id</code></summary>
<p>Deleta um aluno do banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `204 NO CONTENT`:

```json
Não há corpo
```

</details>

- ### **Exercícios**

<details>
  <summary>POST <code>/exercise</code></summary>
<p>Cadastra um novo exercício no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Supino Reto",
  "series": 4,
  "repeticoes": 15,
  "carga": "10kg cada lado",
  "estimulo": "Peito",
  "aparelho": "Supino"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "Supino Reto",
  "estimulo": "Peito",
  "aparelho": {
    "id": 1,
    "nome": "Supino",
    "código": 2
  },
  "id": 1,
  "execucao": {
    "series": 4,
    "repeticoes": 15,
    "carga": "10kg cada lado"
  }
}
```

</details>

<details>
  <summary>GET <code>/exercise</code></summary>
<p>Retorna uma lista contendo todos os exercícios cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "exercicios": [
    {
      "id": 1,
      "nome": "Supino Reto",
      "execucao": {
        "series": 4,
        "repetições": 10,
        "carga": "10 kg de cada lado"
      },
      "aparelho": {
        "id": 1,
        "nome": "Supino",
        "código": 2
      }
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/exercise/:id</code></summary>
<p>Retorna as informações do exercício indicado na url.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "id": 1,
  "nome": "Supino Reto",
  "execucao": {
    "series": 4,
    "repetições": 10,
    "carga": "10 kg de cada lado"
  },
  "aparelho": {
    "id": 1,
    "nome": "Supino",
    "código": 2
  }
}
```

</details>

<details>
  <summary>PATCH <code>/exercise/:id</code></summary>
<p>Atualiza as informações de um exercício no banco de dados.</p>
Corpo da requisição:

```json
{
  "repetições": 10
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 1,
  "nome": "Supino Reto",
  "execucao": {
    "series": 4,
    "repeticoes": 10,
    "carga": "10kg de cada lado"
  },
  "aparelho": {
    "id": 1,
    "nome": "Supino",
    "código": 2
  }
}
```

</details>

<details>
  <summary>DELETE <code>/exercise/:id</code></summary>
<p>Deleta um exercício do banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `204 NO CONTENT`:

```json
Não há corpo
```

</details>

- ### **Treinos**

<details>
  <summary>POST <code>/training</code></summary>
<p>Cadastra um novo treino no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "A",
  "personal": "José Alves Santos",
  "aluno": "Antonio Luiz",
  "dia": "Segunda-Feira",
  "exercicios": ["Supino Reto", "Peck Deck"]
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "A",
  "personal": {
    "nome": "José Alvez",
    "email": "jose@alves.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 1.75,
    "IMC": 26.12
  },
  "dia": "Segunda-Feira",
  "exercicios": [
    {
      "id": 1,
      "nome": "Supino Reto",
      "execucao": {
        "id": 1,
        "series": 3,
        "repeticoes": 10,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 1,
        "nome": "Supino",
        "código": 2
      }
    },
    {
      "id": 2,
      "nome": "Pack Deck",
      "execucao": {
        "id": 2,
        "series": 4,
        "repeticoes": 12,
        "carga": "40kg"
      },
      "aparelho": {
        "id": 2,
        "nome": "Pack Deck",
        "código": 5
      }
    }
  ],
  "id": 1
}
```

</details>

<details>
  <summary>GET <code>/training</code></summary>
<p>Retorna uma lista contendo todos os treinos cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "treinos": [
    {
      "id": 1,
      "nome": "A",
      "personal": {
        "nome": "Jose Alvez",
        "email": "jose@alves.com",
        "cpf": "333.333.333-33"
      },
      "aluno": {
        "nome": "Antonio luiz",
        "telefone": "(99)99999-9999",
        "email": "antonio@email.com",
        "peso": 80,
        "altura": 1.75,
        "imc": 26.12
      },
      "exercicios": [
        {
          "id": 3,
          "nome": "Crossover",
          "execucao": {
            "id": 3,
            "series": 3,
            "repeticoes": 15,
            "carga": "5kg de cada lado"
          },
          "aparelho": {
            "id": 3,
            "nome": "Cross",
            "código": 8
          }
        },
        {
          "id": 2,
          "nome": "Pack Deck",
          "execucao": {
            "id": 2,
            "series": 4,
            "repeticoes": 12,
            "carga": "40kg"
          },
          "aparelho": {
            "id": 2,
            "nome": "Pack Deck",
            "código": 5
          }
        }
      ]
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/training/:id</code></summary>
<p>Retorna as informações do treino indicado na url.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "id": 1,
  "nome": "A",
  "personal": {
    "nome": "Jose Alvez",
    "email": "jose@alves.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "nome": "Antonio luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 1.75,
    "imc": 26.12
  },
  "exercicios": [
    {
      "id": 3,
      "nome": "Crossover",
      "execucao": {
        "id": 3,
        "series": 3,
        "repeticoes": 15,
        "carga": "5kg de cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Cross",
        "código": 8
      }
    },
    {
      "id": 2,
      "nome": "Pack Deck",
      "execucao": {
        "id": 2,
        "series": 4,
        "repeticoes": 12,
        "carga": "40kg"
      },
      "aparelho": {
        "id": 2,
        "nome": "Pack Deck",
        "código": 5
      }
    }
  ]
}
```

</details>

<details>
  <summary>PATCH <code>/training/:id</code></summary>
<p>Atualiza as informações de um treino no banco de dados.</p>
Corpo da requisição:

```json
{
  "exercicios": ["Crossover", "Pack Deck"]
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "exercicios": [
    {
      "id": 3,
      "repetições": "15",
      "series": 3,
      "nome": "Crossover",
      "carga": "5kg de cada lado",
      "aparelho": {
        "id": 3,
        "nome": "Cross",
        "código": 8
      }
    },
    {
      "id": 2,
      "nome": "Peck Deck",
      "series": 4,
      "repetições": "12",
      "carga": "40kg",
      "aparelho": {
        "id": 2,
        "nome": "Pack Deck",
        "código": 5
      }
    }
  ],
  "id": 1,
  "nome": ["A"],
  "personal": {
    "nome": "Jose Alvez",
    "email": "jose@alves.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 1.75,
    "imc": 26.12
  }
}
```

</details>

<details>
  <summary>DELETE <code>/training/:id</code></summary>
<p>Deleta um treino do banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `204 NO CONTENT`:

```json
Não há corpo
```

</details>

- ### **Equipamentos**

<details>
  <summary>POST <code>/equipment</code></summary>
<p>Cadastra um novo equipamento no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Supino",
  "codigo": 1
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "Supino",
  "codigo": 1,
  "id": 1
}
```

</details>

<details>
  <summary>GET <code>/equipment</code></summary>
<p>Retorna uma lista contendo todos os equipamentos cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "equipamentos": [
    {
      "id": 1,
      "nome": "Máquina de Supino",
      "codigo": 1
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/equipment/:id</code></summary>
<p>Retorna as informações do equipamento indicado na url.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "id": 1,
  "nome": "Máquina de Supino",
  "codigo": 1
}
```

</details>

<details>
  <summary>PATCH <code>/equipment/:id</code></summary>
<p>Atualiza as informações de um equipamento no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Máquina de Supino"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "nome": "Máquina de Supino",
  "codigo": 1,
  "id": 1
}
```

</details>

<details>
  <summary>DELETE <code>/equipment/:id</code></summary>
<p>Deleta um equipamento do banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `204 NO CONTENT`:

```json
Não há corpo
```

</details>
