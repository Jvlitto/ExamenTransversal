function validar_vacuna()
{
    var id = document.formulario.txt_id.value
    var marca = document.formulario.txt_marca.value
    var laboratorio = document.formulario.txt_laboratorio.value
    var stock = document.formulario.txt_stock.value
    var fecha_elab = document.formulario.txt_fechaelab.value
    var fecha_ven = document.formulario.txt_fechaven.value
    var today = new Date
    

    if (id.length<2)
    {
        alert("ID debe tener al menos 2 caracteres");
        document.formulario.txt_id.focus();
        return false;
    }
    if (marca.length<3)
    {
        alert("Marca debe tener al menos 3 caracteres");
        document.formulario.txt_marca.focus();
        return false;
    }
    if (laboratorio.length<3)
    {
        alert("Marca debe tener al menos 3 caracteres");
        document.formulario.txt_laboratorio.focus();
        return false;
    }
    if (stock.length<2)
    {
        alert("El Stock debe ser mayor a 99 unidades");
        document.formulario.txt_stock.focus();
        return false;
    }
    if (fecha_elab >= today)
    {
        alert("Fecha de Elaboración NO puede ser igual o mayor a Hoy");
        document.formulario.txt_fechaelab.focus();
        return false;
    }
    if (fecha_ven <= today)
    {
        alert("Fecha de Vencimiento NO puede ser igual o menor a Hoy");
        document.formulario.txt_fechaven.focus();
        return false;
    }
    alert("Todo correctamente ingresado")
    document.formulario.action = "/ingreso_vacuna/"
    document.formulario.submit() = true;
}

function buscar_vac()
{
    var marca = document.formulario.txt_marca.value

    if (marca.length<3)
    {
        alert("la Marca debe tener al menos 3 caracteres");
        document.formulario.txt_marca.focus();
        return false;
    }
    alert("Todo correctamente ingresado")
    document.formulario.action = "/buscar_vacuna/"
    document.formulario.submit() = true;
}

function eliminar_vac()
{
    var id = document.formulario.txt_id.value

    if (id.length<2)
    {
        alert("ID debe tener al menos 2 caracteres");
        document.formulario.txt_id.focus();
        return false;
    }
    alert("Vacuna correctamente eliminada")
    document.formulario.action = "/eliminacion_vacuna/"
    document.formulario.submit() = true;
}

function modificar_vacuna()
{
    var id = document.formulario.txt_id.value
    var stock = document.formulario.txt_stock.value
    var fecha_elab = document.formulario.txt_fechaelab.value
    var fecha_ven = document.formulario.txt_fechaven.value
    var today = new Date

    if (id.length<2)
    {
        alert("ID debe tener al menos 2 caracteres");
        document.formulario.txt_id.focus();
        return false;
    }
    if (stock.length<2)
    {
        alert("El Stock debe ser mayor a 99 unidades");
        document.formulario.txt_stock.focus();
        return false;
    }
    if (fecha_elab>=today)
    {
        alert("Fecha de Elaboración NO puede ser igual o mayor a Hoy");
        document.formulario.txt_fechaelab.focus();
        return false;
    }
    if (fecha_ven<=today)
    {
        alert("Fecha de Vencimiento NO puede ser igual o menor a Hoy");
        document.formulario.txt_fechaven.focus();
        return false;
    }
    alert("Vacuna Modificada Correctamente")
    document.formulario.action = "/modificar_vacuna/"
    document.formulario.submit() = true;
}