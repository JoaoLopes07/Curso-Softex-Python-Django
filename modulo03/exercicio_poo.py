class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
            print(f"✅ Sucesso: Email alterado para {self.__email}")
        else:
            print(f"❌ Erro: O email '{novo_email}' é inválido (falta @).")

class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("As subclasses devem implementar o método enviar()")

class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📧 Enviando para servidor de email: {mensagem}")

class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📱 Enviando para operadora telefônica: {mensagem}")

class SistemaAlerta:
    def __init__(self, usuario, canal):
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto):
        print(f"--- Iniciando alerta para usuário: {self.usuario.nome} ---")
        self.canal.enviar(texto)
        print("-------------------------------------------------------")

if __name__ == "__main__":
    print(">>> 1. TESTE DE SEGURANÇA")
    user_dev = Usuario("Carlos Developer", "carlos@startup.com")
    
    user_dev.email = "carlos-sem-arroba" 
    
    user_dev.email = "carlos.admin@startup.com"
    print("\n")

    print(">>> 2. TESTE DE EMAIL")
    canal_email = Email()
    
    sistema_v1 = SistemaAlerta(user_dev, canal_email)
    sistema_v1.disparar("Alerta Crítico: O Servidor DB-01 caiu!")
    print("\n")

    print(">>> 3. TESTE DE SMS")
    canal_sms = SMS()
    
    sistema_v2 = SistemaAlerta(user_dev, canal_sms)
    sistema_v2.disparar("Aviso: Seu pagamento foi aprovado.")