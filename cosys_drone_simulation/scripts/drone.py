import cosysairsim as airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

print("Decolando...")
client.takeoffAsync().join()

ALTITUDE = -8
client.moveToZAsync(ALTITUDE, 2).join()

VELOCIDADE = 3
TAMANHO_GRID = 50
ESPACO_LINHAS = 10

print(
    f"Iniciando varredura da plantação a {abs(ALTITUDE)} metros de altura...")

for x in range(0, TAMANHO_GRID + 1, ESPACO_LINHAS):
    print(f"Percorrendo linha X: {x}")
    client.moveToPositionAsync(x, TAMANHO_GRID, ALTITUDE, VELOCIDADE).join()

    proximo_x = x + ESPACO_LINHAS
    if proximo_x <= TAMANHO_GRID:
        client.moveToPositionAsync(
            proximo_x, TAMANHO_GRID, ALTITUDE, VELOCIDADE).join()

        print(f"Voltando linha X: {proximo_x}")
        client.moveToPositionAsync(proximo_x, 0, ALTITUDE, VELOCIDADE).join()

print("Varredura completa! Retornando para a base...")
client.moveToPositionAsync(0, 0, ALTITUDE, VELOCIDADE).join()
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)
print("Drone em segurança.")
