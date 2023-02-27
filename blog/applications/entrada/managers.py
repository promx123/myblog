from django.db import  models

class EntryManager(models.Manager):
    #mangarer de entrada
    
    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,
            
        ).order_by('-created').first() #esta ordenado con el timestampedmodel
        
    def entradas_en_home(self):
        #devuelve las ultimas entradas al home
        return self.filter(
            public = True,
            in_home = True,
        ).order_by('-created')[:4] #retorna los primeros 4 y 4: retorna los ultimos 4
        
    def entradas_recientes(self):
        #devuelve las ultimas 6 entradas recientes
        return self.filter(
            public = True,
        ).order_by('-created')[:6]
        
    def buscar_entradas(self, kword, categoria):
        #busqueda por categorio o kword
        if len(categoria)>0:
            return self.filter(
                category__short_name = categoria, #filtrado directamente del modelo
                title__icontains = kword,
                public = True,
            ).order_by('-created')
            
        else:
             return self.filter(
                title__icontains = kword,
                public = True,
            ).order_by('-created')