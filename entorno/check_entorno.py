"""Smoke test del entorno: imports, dispositivo, un paso de entrenamiento, Haar cascade y MFCC."""
import importlib, sys
mods = ["torch", "torchvision", "numpy", "pandas", "matplotlib", "seaborn",
        "sklearn", "PIL", "cv2", "librosa", "soundfile", "gdown", "tqdm"]
bad = []
for m in mods:
    try:
        mod = importlib.import_module(m)
        print(f"OK  {m:12s} {getattr(mod, '__version__', '')}")
    except Exception as e:
        bad.append(m); print(f"FALTA {m}: {e}")
if bad:
    sys.exit(f"Faltan paquetes: {bad}")

import torch, torch.nn as nn, numpy as np, cv2, librosa
device = ("mps" if torch.backends.mps.is_available()
          else "cuda" if torch.cuda.is_available() else "cpu")
print("Dispositivo para entrenar:", device)

net = nn.Sequential(nn.Conv2d(3, 8, 3), nn.ReLU(), nn.Flatten(), nn.LazyLinear(7)).to(device)
opt = torch.optim.Adam(net.parameters(), 1e-3)
x = torch.randn(4, 3, 100, 100, device=device); y = torch.randint(0, 7, (4,), device=device)
loss = nn.CrossEntropyLoss()(net(x), y); loss.backward(); opt.step()
print("Paso de entrenamiento CNN OK, loss =", round(loss.item(), 3))

casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print("Haar cascade cargado:", not casc.empty())

sig = np.random.randn(22050 * 3).astype("float32")
mf = librosa.feature.mfcc(y=sig, sr=22050, n_mfcc=40)
print("MFCC OK, forma:", mf.shape)
print("\nTodo listo para el TP3.")
