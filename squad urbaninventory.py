equipamentos = [
    {"id": "Respirador 1", "setor": "UTI", "dias": 45, "revisado": True},
    {"id": "Respirador 2", "setor": "UTI", "dias": 210, "revisado": True},
    {"id": "Bomba 1", "setor": "Triagem", "dias": 30, "revisado": False},
    {"id": "Monitor 1", "setor": "UTI", "dias": 100, "revisado": True}
]

prazo = 180


todos_dentro_prazo = all(equipamento["dias"] <= prazo for equipamento in equipamentos)

print("Todos estão dentro do prazo?", todos_dentro_prazo)



uti_sem_revisao = any(
    equipamento["setor"] == "UTI" and not equipamento["revisado"]
    for equipamento in equipamentos
)

print("Existe equipamento da UTI sem revisão?", uti_sem_revisao)



equipamentos_com_problema = [
    equipamento["id"]
    for equipamento in equipamentos
    if equipamento["dias"] > prazo or not equipamento["revisado"]
]

print("Equipamentos com problema:", equipamentos_com_problema)