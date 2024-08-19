from django.db import models

# Create your models here.


class Responsavel(models.Model):
    class Cargo(models.TextChoices):
        INSTRUTOR = "IN", "Instrutor"
        MONITOR = "MO", "Monitor"

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    cargo = models.CharField(max_length=2, choices=Cargo.choices)

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"

    def __str__(self):
        return self.user.username


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.ManyToManyField(Responsavel)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self):
        return f"{self.nome}"


class Imersionista(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    rgm = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f"{self.nome} - {self.rgm} - {self.turma} "


class Presenca(models.Model):
    class Situacao(models.TextChoices):
        PRESENTE = "PR", "Presente"
        AUSENTE = "AU", "Ausente"
        JUSTIFICADO = "JU", "Justificado"

    aluno = models.ForeignKey(Imersionista, on_delete=models.CASCADE)
    data = models.DateField()
    situacao = models.CharField(max_length=2, choices=Situacao.choices)

    class Meta:
        verbose_name = "Presença"
        verbose_name_plural = "Presenças"

    def __str__(self):
        return f"{self.aluno.nome} - {self.data} - {self.situacao}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Verifica se já existe uma presença para o aluno nesta data, apenas no caso de criação
            if Presenca.objects.filter(aluno=self.aluno, data=self.data).exists():
                raise ValueError(
                    "A presença para este aluno nesta data já foi registrada."
                )
        else:
            # Impede a alteração da data durante uma atualização
            original = Presenca.objects.get(pk=self.pk)
            if original.data != self.data:
                raise ValueError(
                    "Não é permitido alterar a data de uma presença existente."
                )

        super().save(*args, **kwargs)
