Seminario de Integración 🚀
Autor: Antoni Fernandez


¡Bienvenidos al repositorio oficial de la materia Seminario de Integración! Este espacio está diseñado para consolidar conocimientos avanzados mediante el desarrollo de aplicaciones web modernas, conectando un backend robusto de alto rendimiento con un frontend reactivo y tipado.

📚 Tecnologías del Curso y Mini-Conceptos

1. Python

¿Qué es? Es un lenguaje de programación de alto nivel, interpretado y multiparadigma, conocido por su sintaxis limpia y legible que enfatiza la productividad del desarrollador.

Uso en el seminario: Base para la lógica de servidor, estructuración de datos y soporte de herramientas modernas de gestión de paquetes como uv.

2. FastAPI

¿Qué es? Un framework web moderno y de alto rendimiento para construir APIs con Python, basado en las anotaciones de tipos estándar de Python (Type Hints).

Uso en el seminario: Construcción de endpoints RESTful rápidos, documentación automática interactiva (Swagger UI / ReDoc) y validación automática de datos mediante Pydantic.

3. Angular

¿Qué es? Una plataforma y framework de desarrollo frontend basado en TypeScript, mantenido por Google, ideal para crear aplicaciones web escalables de una sola página (SPA).

Uso en el seminario: Desarrollo de la interfaz de usuario basada en componentes, gestión de formularios, consumo de servicios HTTP y enrutamiento dinámico.

🗂️ Estructura del Repositorio

El proyecto está organizado para soportar arquitecturas modulares o multi-proyecto (monorepo), permitiendo separar claramente los servicios de backend y frontend:

/
├── backend/          # FastAPI & Python (con gestión uv)
├── frontend/         # Angular application
└── .gitignore        # Exclusiones globales de Git


⚙️ Requisitos Previos

Asegúrate de tener instalado en tu entorno local:

Python (versión recomendada 3.10 o superior)

Node.js y npm (para Angular CLI)

uv (gestor ultrarrápido de paquetes y entornos virtuales de Python)

🚀 Primeros Pasos

Clona este repositorio en tu máquina local.

Configura tu entorno virtual backend utilizando uv:

cd backend
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
uv pip install -r requirements.txt


Instala las dependencias del frontend:

cd ../frontend
npm install


¡Listo para comenzar con las prácticas y proyectos integradores!