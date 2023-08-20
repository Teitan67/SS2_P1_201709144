crearModelo = [
"""
create table GeneralData(
	EntregaId int,
	Dia varchar(20),
	Mes varchar(20),
	Anio varchar(10),
	NombreCliente varchar(50),
	Direccion varchar(80),
	NomreEmpleadoEntrega varchar(80),
	PuestoEmpleadoEntrega varchar(40),
	CiudadEntrega varchar(50),
	NombreProducto varchar(50),
	Descripcion varchar(80),
	Peso decimal(10,2),
	TiempoEntrega int,
	EstadoEntrega varchar(50),
	CostoEnvio decimal(10,2),
	PrecioProducto decimal(10,2)
)
""",
"""
create table Cliente(
	IdCliente int IDENTITY(1,1) primary key,
	Nombre varchar(50)
)
""",
"""
create table Direccion(
	IdDireccion int IDENTITY(1,1) primary key,
	Direccion varchar(80),
	Ciudad varchar(50)
)
""",
"""
create table Producto(
	IdProducto int IDENTITY(1,1) primary key,
	Nombre varchar(80),
	Descripcion varchar(80),
	Peso decimal(10,2),
	Precio decimal(10,2)
)
""",
"""
create table Fecha(
	IdFecha int IDENTITY(1,1) primary key,
	Dia varchar(20),
	Mes varchar(20),
	Anio varchar(10)
)
""",
"""
create table Empleado(
	IdEmpleado int IDENTITY(1,1) primary key,
	Nombre varchar(80),
	Puesto varchar(50)
)
""",
"""
create table EstadoEntrega(
	IdEstado int IDENTITY(1,1) primary key,
	Estado varchar(40)
)
""",
"""
create table Entregas(
	IdEntrega int IDENTITY(1,1) primary key,
	Entrega int,
	Fecha int,
	Cliente int,
	Empleado int,
	Direccion int,
	Producto int,
	EstadoEntrega int,
	TiempoEntrega int,
	CostoEnvio decimal(10,2),
	foreign key (Cliente) references Cliente(IdCliente),
	foreign key (Direccion) references Direccion(IdDireccion),
	foreign key (Producto) references Producto(IdProducto),
	foreign key (Fecha) references Fecha(IdFecha),
	foreign key (Empleado) references Empleado(IdEmpleado),
	foreign key (EstadoEntrega) references EstadoEntrega(IdEstado)
)
"""
]

borrarModelo = [
"drop table GeneralData",
"drop table Cliente",
"drop table Direccion",
"drop table Producto",
"drop table Fecha",
"drop table Empleado",
"drop table EstadoEntrega",
"drop table Entregas"
]

cargarInformacion = [
    """
    insert into Cliente(Nombre) select G.NombreCliente from GeneralData G group by G.NombreCliente
    """,
    """
	insert into Direccion(Direccion,Ciudad) select G.Direccion,G.CiudadEntrega from GeneralData G group by G.Direccion,G.CiudadEntrega 
	""",
    """
	insert into Producto(Nombre,Descripcion,Peso,Precio) select G.NombreProducto,G.Descripcion,G.Peso,G.PrecioProducto from GeneralData G where G.NombreProducto != ''   group by G.NombreProducto,G.Descripcion,G.Peso,G.PrecioProducto 
	""",
    """
	insert into Fecha(Anio,Mes,Dia) select G.Anio,G.Mes,G.Dia from GeneralData G where G.Anio !=''  group by G.Anio,G.Mes,G.Dia 
	""",
    """
	insert into Empleado(Nombre,Puesto) select G.NomreEmpleadoEntrega,G.PuestoEmpleadoEntrega from GeneralData G    group by G.NomreEmpleadoEntrega,G.PuestoEmpleadoEntrega 
	""",
    """
	insert into EstadoEntrega(Estado) select G.EstadoEntrega from GeneralData G where G.EstadoEntrega!='' group by G.EstadoEntrega 	
	""",
    """
	"""
]
consulta1="""
select
	(select count(*) from GeneralData) as Registros,
	(select count(*) from Cliente) as Clientes,
	(select count(*) from Direccion) as Direcciones,
	(select count(*) from Producto) as Productos,
	(select count(*) from Fecha) as Fechas,
	(select count(*) from Empleado) as Empleados,
	(select count(*) from EstadoEntrega) as EstadosEntregas,
	(select count(*) from Entregas) as Entregas
"""
consulta2 = """
SELECT TOP 5
    C.Nombre AS NombreCliente,
    COUNT(E.IdEntrega) AS TotalEntregas
FROM
    Cliente AS C
JOIN
    Entregas AS E ON C.IdCliente = E.Cliente
WHERE
    E.EstadoEntrega = 1
GROUP BY
    C.Nombre
ORDER BY
    TotalEntregas DESC
"""

consulta4 = """

select 
	C.Name_ as Country,
	AVG(T.TotalDamage_)as PromDamage 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	C.Name_
order by 
	AVG(T.TotalDamage_) desc

"""

consulta5 = """
select 
top 5
	C.Name_ as Pais,
	SUM(T.TotalDeaths_)as MuertesTotales 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	C.Name_
order by 
	MuertesTotales desc
"""

consulta6 = """
select 
top 5
	D.Year_ as ANIOS,
	sum(T.TotalDeaths_)as MuertesTotales 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	D.Year_
order by 
	MuertesTotales desc
"""

consulta7="""
select 
top 5
	D.Year_ as ANIOS,
	count(T.TotalDeaths_)as TotalTsunamis 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	D.Year_
order by 
	TotalTsunamis desc
"""

consulta8="""
select 
top 5
	C.Name_ as Pais,
	sum(T.TotalHouseDestroy_)as TotalCasasDestruidas 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	C.Name_
order by 
	TotalCasasDestruidas desc
"""

consulta9="""
select 
top 5
	C.Name_ as Pais,
	sum(T.TotalHouseDamage_)as TotalHouseDamage 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	C.Name_
order by 
	TotalHouseDamage desc
"""

consulta10 = """

select 
	C.Name_ as Pais,
	avg(T.MaxWaterHeight_)as MaxWaterHeight 
from 
	TS_Tsunami T, 
	TS_DateTime D,
	TS_Country C
where 
	T.DateTime_=D.Id_  and
	T.Country_ = C.Id_
group by 
	C.Name_
order by 
	MaxWaterHeight desc
"""