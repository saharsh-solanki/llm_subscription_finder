import os
import sys

from repo.vector_db import VectorDBRepo

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

obj = VectorDBRepo()
obj.store_plans()