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
  "nome": "Lucas Pereira",
  "email": "Lucas@email.com",
  "cpf": "333.333.333-34",
  "senha": "*aA123456"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 3,
  "nome": "Lucas Pereira",
  "email": "Lucas@email.com",
  "cpf": "333.333.333-34",
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
      "nome": "Augusto Pereira",
      "email": "Augusto@email.com",
      "cpf": "333.333.333-33",
      "alunos": []
    },
    {
      "id": 3,
      "nome": "Lucas Pereira",
      "email": "Lucas@email.com",
      "cpf": "333.333.333-34",
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
  "id": 3,
  "nome": "Lucas Pereira",
  "email": "Lucas@email.com",
  "cpf": "333.333.333-34",
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
  "email": "Lucas@email.com",
  "senha": "*aA123456"
}
```

Corpo da resposta `200 OK`:

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTgwNDExNiwianRpIjoiOTE5ZDMyZTEtZTBiZS00ODE2LWIxZmMtNDY5MjUwNDUxNmJjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6Mywibm9tZSI6Ikx1Y2FzIFBlcmVpcmEiLCJlbWFpbCI6Ikx1Y2FzQGVtYWlsLmNvbSIsImNwZiI6IjMzMy4zMzMuMzMzLTM0IiwiYWx1bm9zIjpbXX0sIm5iZiI6MTY1MTgwNDExNiwiZXhwIjoxNjUxODA3NzE2fQ.M4lOkNw83LL4zOvysrrHQGL7TRJKPtvxbGlEu3MWP60",
  "user": {
    "id": 3,
    "nome": "Lucas Pereira",
    "email": "Lucas@email.com",
    "cpf": "333.333.333-34",
    "alunos": []
  }
}
```

</details>

<details>
  <summary>PATCH <code>/personal</code></summary>
<p>Atualiza as informações de um personal já cadastrado no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Lucas Pereira Silva"
}
```

Corpo da resposta `200 OK`:

```json
{
  "id": 3,
  "nome": "Lucas Pereira Silva",
  "email": "Lucas@email.com",
  "cpf": "333.333.333-34",
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
  <summary>POST <code>/alunos</code></summary>
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
  "altura": 2.0,
  "imc": 26.0,
  "personal": {
    "id": 1,
    "nome": "Augusto Pereira",
    "cpf": "333.333.333-33"
  },
  "treinos": []
}
```

</details>

<details>
  <summary>GET <code>/alunos</code></summary>
<p>Retorna uma lista contendo todos os alunos cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "count": 2,
  "alunos": [
    {
      "id": 1,
      "nome": "Antonio Ruiz",
      "telefone": "(99)99999-9999",
      "email": "antonio@email.com",
      "peso": 80,
      "altura": 2.0,
      "imc": 26.0,
      "treinos": []
    },
    {
      "id": 2,
      "nome": "Carlos Barbosa",
      "telefone": "(99)99999-9999",
      "email": "Carlos@email.com",
      "peso": 80,
      "altura": 2.0,
      "imc": 26.0,
      "treinos": []
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/alunos/:id</code></summary>
<p>Retorna as informações do aluno indicado na url.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
{
  "id": 1,
  "nome": "Antonio Ruiz",
  "telefone": "(99)99999-9999",
  "email": "antonio@email.com",
  "peso": 80,
  "altura": 2.0,
  "imc": 26.0,
  "personal": {
    "id": 1,
    "nome": "Augusto Pereira",
    "cpf": "333.333.333-33"
  },
  "treinos": []
}
```

</details>

<details>
  <summary>PATCH <code>/alunos</code></summary>
<p>Atualiza as informações de um aluno no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Antonio Luiz"
}
```

Corpo da resposta `200 OK`:

```json
{
  "id": 1,
  "nome": "Antonio Luiz",
  "telefone": "(99)99999-9999",
  "email": "antonio@email.com",
  "peso": 80,
  "altura": 2.0,
  "imc": 26.0,
  "treinos": []
}
```

</details>

<details>
  <summary>DELETE <code>/alunos/:id</code></summary>
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
  <summary>POST <code>/exercicio</code></summary>
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
  "id": 1,
  "nome": "Supino Reto",
  "estimulo": "Peito",
  "execucao": {
    "id": 1,
    "series": 4,
    "repeticoes": 15,
    "carga": "10kg cada lado"
  },
  "aparelho": {
    "id": 3,
    "nome": "Supino",
    "codigo": 2
  }
}
```

</details>

<details>
  <summary>GET <code>/exercicio</code></summary>
<p>Retorna uma lista contendo todos os exercícios cadastrados no banco de dados.</p>
Corpo da requisição:

```json
Não há corpo
```

Corpo da resposta `200 OK`:

```json
[
  {
    "id": 1,
    "nome": "Supino Reto",
    "estimulo": "Peito",
    "execucao": {
      "id": 1,
      "series": 4,
      "repeticoes": 15,
      "carga": "10kg cada lado"
    },
    "aparelho": {
      "id": 3,
      "nome": "Supino",
      "codigo": 2
    }
  },
  {
    "id": 2,
    "nome": "Supino Inclinado",
    "estimulo": "Peito",
    "execucao": {
      "id": 2,
      "series": 4,
      "repeticoes": 15,
      "carga": "10kg cada lado"
    },
    "aparelho": {
      "id": 3,
      "nome": "Supino",
      "codigo": 2
    }
  }
]
```

</details>

<details>
  <summary>GET <code>/exercicio/:id</code></summary>
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
  "estimulo": "Peito",
  "execucao": {
    "id": 1,
    "series": 4,
    "repeticoes": 15,
    "carga": "10kg cada lado"
  },
  "aparelho": {
    "id": 3,
    "nome": "Supino",
    "codigo": 2
  }
}
```

</details>

<details>
  <summary>PATCH <code>/exercicio/:id</code></summary>
<p>Atualiza as informações de um exercício no banco de dados.</p>
Corpo da requisição:

```json
{
  "repeticoes": 10
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 1,
  "nome": "Supino Reto",
  "estimulo": "Peito",
  "execucao": {
    "id": 1,
    "series": 4,
    "repeticoes": 10,
    "carga": "10kg cada lado"
  },
  "aparelho": {
    "id": 3,
    "nome": "Supino",
    "codigo": 2
  }
}
```

</details>

<details>
  <summary>DELETE <code>/exercicio/:id</code></summary>
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
  <summary>POST <code>/treino</code></summary>
<p>Cadastra um novo treino no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "A",
  "personal_id": "1",
  "aluno_id": "1",
  "email_aluno": "antonio@email.com",
  "dia": "Segunda-Feira",
  "exercicios": ["Supino", "Supino Inclinado"]
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 1,
  "nome": "A",
  "dia": "Segunda-Feira",
  "personal": {
    "id": 1,
    "nome": "Augusto Pereira",
    "email": "Augusto@email.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "id": 1,
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 2.0,
    "imc": 26.0,
    "treinos": [
      {
        "id": 1,
        "nome": "A",
        "dia": "Segunda-Feira"
      }
    ]
  },
  "exercicios": [
    {
      "id": 2,
      "nome": "Supino Inclinado",
      "estimulo": "Peito",
      "execucao": {
        "id": 2,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    },
    {
      "id": 3,
      "nome": "Supino",
      "estimulo": "Peito",
      "execucao": {
        "id": 3,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/treino</code></summary>
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
      "dia": "Segunda-Feira",
      "personal": {
        "id": 1,
        "nome": "Augusto Pereira",
        "email": "Augusto@email.com",
        "cpf": "333.333.333-33"
      },
      "aluno": {
        "id": 1,
        "nome": "Antonio Luiz",
        "telefone": "(99)99999-9999",
        "email": "antonio@email.com",
        "peso": 80,
        "altura": 2.0,
        "imc": 26.0,
        "treinos": [
          {
            "id": 1,
            "nome": "A",
            "dia": "Segunda-Feira"
          }
        ]
      },
      "exercicios": [
        {
          "id": 2,
          "nome": "Supino Inclinado",
          "estimulo": "Peito",
          "execucao": {
            "id": 2,
            "series": 4,
            "repeticoes": 15,
            "carga": "10kg cada lado"
          },
          "aparelho": {
            "id": 3,
            "nome": "Supino",
            "codigo": 2
          }
        },
        {
          "id": 3,
          "nome": "Supino",
          "estimulo": "Peito",
          "execucao": {
            "id": 3,
            "series": 4,
            "repeticoes": 15,
            "carga": "10kg cada lado"
          },
          "aparelho": {
            "id": 3,
            "nome": "Supino",
            "codigo": 2
          }
        }
      ]
    }
  ]
}
```

</details>

<details>
  <summary>GET <code>/treino/:id</code></summary>
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
  "dia": "Segunda-Feira",
  "personal": {
    "id": 1,
    "nome": "Augusto Pereira",
    "email": "Augusto@email.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "id": 1,
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 2.0,
    "imc": 26.0,
    "treinos": [
      {
        "id": 1,
        "nome": "A",
        "dia": "Segunda-Feira"
      }
    ]
  },
  "exercicios": [
    {
      "id": 2,
      "nome": "Supino Inclinado",
      "estimulo": "Peito",
      "execucao": {
        "id": 2,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    },
    {
      "id": 3,
      "nome": "Supino",
      "estimulo": "Peito",
      "execucao": {
        "id": 3,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    }
  ]
}
```

</details>

<details>
  <summary>PATCH <code>/treino/:id</code></summary>
<p>Atualiza as informações de um treino no banco de dados.</p>
Corpo da requisição:

```json
{
  "exercicios": ["Barra", "Barra Inclinada"]
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 1,
  "nome": "A",
  "dia": "Segunda-Feira",
  "personal": {
    "id": 1,
    "nome": "Augusto Pereira",
    "email": "Augusto@email.com",
    "cpf": "333.333.333-33"
  },
  "aluno": {
    "id": 1,
    "nome": "Antonio Luiz",
    "telefone": "(99)99999-9999",
    "email": "antonio@email.com",
    "peso": 80,
    "altura": 2.0,
    "imc": 26.0,
    "treinos": [
      {
        "id": 1,
        "nome": "A",
        "dia": "Segunda-Feira"
      }
    ]
  },
  "exercicios": [
    {
      "id": 4,
      "nome": "Barra",
      "estimulo": "Peito",
      "execucao": {
        "id": 4,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    },
    {
      "id": 6,
      "nome": "Barra Inclinada",
      "estimulo": "Peito",
      "execucao": {
        "id": 6,
        "series": 4,
        "repeticoes": 15,
        "carga": "10kg cada lado"
      },
      "aparelho": {
        "id": 3,
        "nome": "Supino",
        "codigo": 2
      }
    }
  ]
}
```

</details>

<details>
  <summary>DELETE <code>/treino/:id</code></summary>
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
  <summary>POST <code>/equipamentos</code></summary>
<p>Cadastra um novo equipamento no banco de dados.</p>
Corpo da requisição:

```json
{
  "nome": "Supino",
  "codigo": 2
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 3,
  "nome": "Supino",
  "codigo": 2
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
  "count": 2,
  "equipments": [
    {
      "id": 1,
      "nome": "Barra Lateral",
      "codigo": 1
    },
    {
      "id": 3,
      "nome": "Supino",
      "codigo": 2
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
  "nome": "Barra Reta",
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
  "nome": "Barra Fixa"
}
```

Corpo da resposta `201 CREATED`:

```json
{
  "id": 1,
  "nome": "Barra Fixa",
  "codigo": 1
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
