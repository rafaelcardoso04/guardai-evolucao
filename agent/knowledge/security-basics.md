# Fundamentos de Segurança

## Conceitos
- **Vulnerabilidade**: fraqueza em um sistema que pode ser explorada.
- **Ameaça**: algo ou alguém que pode explorar a vulnerabilidade.
- **Risco**: chance de a ameaça explorar a vulnerabilidade × o dano causado.

## Tríade CIA
- **Confidencialidade**: só quem tem permissão acessa a informação.
- **Integridade**: a informação não é alterada indevidamente.
- **Disponibilidade**: o sistema e os dados estão acessíveis quando necessários.

## Boas práticas
- Princípio do menor privilégio.
- Validar e tratar toda entrada; usar consultas parametrizadas contra SQL Injection.
- Manter sistemas atualizados e com patches aplicados.
- Senhas com hash forte e autenticação multifator.
- Registrar logs e monitorar acessos.
- Reduzir a superfície de ataque: fechar portas e serviços desnecessários.
- Fazer backups e testar a restauração.
- Testar apenas em ambientes próprios ou autorizados.
