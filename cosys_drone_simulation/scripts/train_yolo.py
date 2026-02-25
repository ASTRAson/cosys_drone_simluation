from ultralytics import YOLO
import os


def train_model():
    # Carrega o modelo
    model = YOLO("yolo11n.pt")

    # Define o caminho do dataset
    caminho_data = "D:/airsim_fazenda/trained_dataset/data.yaml"

    print("Iniciando o treinamento do detector de abacaxis...")

    # Inicia o treinamento
    results = model.train(
        data=os.path.normpath(caminho_data),
        epochs=100,
        imgsz=640,
        device=0,
        project="Tese_OpenRAN",
        name="v1_abacaxi_detec",
        batch=4,
        workers=2
    )

    print("Treino finalizado! O melhor modelo está salvo na pasta 'runs'.")


if __name__ == '__main__':
    train_model()
