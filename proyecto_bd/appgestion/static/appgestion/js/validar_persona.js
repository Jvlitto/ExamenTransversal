//----------Funcion Validar Personas (Formulario Ingreso)----------//
function validar_persona()
{
    var rut = document.formulario.txt_rut.value
    var nombre = document.formulario.txt_nombre.value
    var apellido_paterno = document.formulario.txt_appaterno.value
    var apellido_materno = document.formulario.txt_apmaterno.value
    var edad = document.formulario.txt_edad.value
    var vacuna = document.formulario.txt_vacuna.value

    if (rut.length<9 || rut.length>10 || rut.indexOf('-')<0 || rut.indexOf('.')>0)
    {
        alert("RUT debe tener entre 9 y 10 caracteres, sin puntos y con guión");
        document.formulario.txt_rut.focus();
        return false;
    }

    if (nombre.length<3)
    {
        alert("Nombre debe tener al menos 3 caracteres");
        document.formulario.txt_nombre.focus();
        return false;
    }
    
    if (apellido_paterno.length<3)
    {
        alert("Apellido Paterno debe tener al menos 3 caracteres");
        document.formulario.txt_appaterno.focus();
        return false;
    }
    if (apellido_materno.length<3)
    {
        alert("Apellido Materno debe tener al menos 3 caracteres");
        document.formulario.txt_apmaterno.focus();
        return false;
    }

    if (edad.length<1|| edad.length>2 || edad>99)
    {
        alert("Edad debe tener al menos 1 caracter y no puede superar los 99 años.");
        document.formulario.txt_edad.focus();
        return false;
    }
    if (vacuna.length<3)
    {
        alert("Vacuna debe tener al menos 3 caracteres");
        document.formulario.txt_vacuna.focus();
        return false;
    }
    alert("Todo correctamente ingresado")
    document.formulario.action = "/ingreso_persona/"
    document.formulario.submit() = true;
    
}

//----------Función Borrar Personas de la BD----------//
function borrar_rut()
{
    var rut = document.formulario.txt_rut.value
    var checkbox1 = document.formulario.checkbox1.value
    if (rut.length<9 || rut.length>10 || rut.indexOf('-')<0)
    {
        alert("RUT debe tener entre 9 y 10 caracteres, sin puntos y con guión");
        document.formulario.txt_rut.focus();
        return false;
    }
    if (checkbox1.checked == false)
    {
        alert("No haz confirmado la eliminación de la persona")
    }
    alert("Persona Correctamente Eliminada")
    document.formulario.action = "/eliminacion_persona/"
    document.formulario.submit() = true;
}


//----------Función Buscar Paciente por Rut----------//
function buscar_rut()
{
    var rut = document.formulario.txt_rut.value

    if (rut.length<9 || rut.length>10 || rut.indexOf('-')<0)
    {
        alert("RUT debe tener entre 9 y 10 caracteres, sin puntos y con guión");
        document.formulario.txt_rut.focus();
        return false;
    }
    alert("Persona Correctamente Buscada")
    document.formulario.action = "/buscar/"
    document.formulario.submit() = true;
}
//----------Función Modificar paciente por Rut-----------//
function modificar_rut()
{
    var rut = document.formulario.txt_rut.value
    var vacuna = document.formulario.txt_vacuna.value

    if (rut.length<9 || rut.length>10 || rut.indexOf('-')<0)
    {
        alert("RUT debe tener entre 9 y 10 caracteres, sin puntos y con guión");
        document.formulario.txt_rut.focus();
        return false;
    }

    if (vacuna.length<3)
    {
        alert("Vacuna debe tener al menos 3 caracteres");
        document.formulario.txt_vacuna.focus();
        return false;
    }
    alert("Persona Correctamente Modificada")
    document.formulario.action = "/modificar/"
    document.formulario.submit() = true;
}