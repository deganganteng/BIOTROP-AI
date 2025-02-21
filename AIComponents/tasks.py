import os
from AIComponents.agents import Agents
from AIComponents.tools import *
from dotenv import load_dotenv
from crewai import Task
from components.subcomponents.urlbase import url

# Load environment variables
load_dotenv()

# Initialize the OpenAI GPT model
openaigpt4 = ChatOpenAI(
    model='gpt-4o',
    temperature=0.2,
    api_key=os.getenv('openapi_key')
)

class Tasks:
    def __init__(self, Input, Context, lang):
    
        self.Input = Input
        self.Context = Context
        self.lang = lang

    def SearchDataTask(self):
        return Task(
            description=f"""
                Lakukan riset dan pencarian data mengenai hasil (KONTEKS) berdasarkan pertanyaan '{self.Input}' 
                dari pengguna, mengenai '{self.Context}'. Gunakan WebsiteSearchTool dan URL terkait untuk membantu pencarian.
            """,
            expected_output=f"""
                Laporan yang detail dan terperinci berdasarkan (KONTEKS).
            """,
            agent=Agents().DataSearch(),
            tools=[WebsiteSearchTool]
        )

    def ContextUserQuer(self):
        return Task(
            description=f"""
                Analisa InputPengguna ini = '{self.Input}'.
                Berikan (KONTEKS) yang jelas dan terarah dari masalah yang berhasil diidentifikasi.
            """,
            expected_output=f"""
                Sebuah Laporan terstruktur yang berisi:
                - Input pengguna original yaitu '{self.Input}'.
                - Penjelasan mengenai apa yang sebenarnya diinginkan oleh pengguna.
                - Penjelasan mengenai apa output yang diharapkan pengguna.
                - Daftar Referensi yang relevan dan bisa digunakan.
            """,
            agent=Agents().Contextualize()
        )

    def AugmentContext(self):
        return Task(
            description=f"""
                Analisa (KONTEKS) yang diberikan, bandingkan dengan '{self.Input}'.
                Gunakan informasi dan referensi yang diberikan untuk lebih memahami (KONTEKS). 
                Buatlah prompt yang terbaik untuk menggenerate response terbaik dalam lingkup '{self.Context}'.
            """,
            expected_output=f"""
                Sebuah Laporan yang berisi:
                - Input pengguna original yaitu '{self.Input}'.
                - Penjelasan mengenai apa yang sebenarnya diinginkan oleh pengguna.
                - Prompt untuk menjawab konteks.
                - Daftar Referensi yang relevan dan bisa digunakan.
            """,
            agent=Agents().Augment()
        )

    def AnalyseAugContext(self):
        return Task(
            description=f"""
                Jawab Input pengguna '{self.Input}' dengan memperhatikan (KONTEKS) berdasarkan sumber informasi yang ada. 
                Gunakan SearchTools untuk mencari informasi tambahan jika diperlukan.
            """,
            expected_output=f"""
                Sebuah lembar Saran dalam '{self.lang}' yang mencakup:
                - Penjelasan mendalam untuk poin kunci dari (KONTEKS).
                - Informasi tambahan terkait '{self.Context}'.
                - Daftar referensi yang digunakan.
            """,
            agent=Agents().Adviser(),
            tools=[WebsiteSearchTool]
        )