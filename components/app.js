const weatherApiKey = "63920dae9a324903aaf234234222904";

$(document).ready(function () {

    $("#form").validate({
        rules: {
            name: {
                required: true,
                minlength: 10
            },
            email: {
                required: true,
                email: true
            },
            numberPhone: {
                required: true,
                number: true,
                min: 0,
                minlength: 9
            },
            city: {
                required: true,
                minlength: 3

            },

            txt_rut: {
                required: true,

            },
            message: {
                required: true,
                minlength: 30
            },
            password:
            {
                required: true,
                minlength: 8,
                formAlphanumeric: true
            },
        },

        messages: {
            name: {
                minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),
                required: "Este campo es requerido"
            },

            email: {
                email: "El email debe tener el formato: abc@domain.tld",
                required: "Este campo es requerido"
            },

            numberPhone: {
                number: "Por favor ingresa un número válido",
                minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),
                required: "Este campo es requerido"
            },
            city: {
                minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),
                required: "Este campo es requerido"
            },
            txt_rut: {
                // minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),
                required: "Este campo es requerido"
            },

            message: {
                minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),
                required: "Este campo es requerido"
            },
            password: {
                required: "Este campo es requerido",
                minlength: jQuery.validator.format("Por favor, al menos {0} caracteres son necesarios"),

            },
        }

    });

    $.validator.addMethod("formAlphanumeric", function (value, element) {
        var pattern = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/; 
        return this.optional(element) || pattern.test(value);
    }, "La contraseña debe y tener al entre 8 y 16 caracteres y 1 letra mayúscula y 1 letra minúscula");

    var Fn = {
        // Valida el rut con su cadena completa "XXXXXXXX-X"
        validaRut: function (rutCompleto) {
            rutCompleto = rutCompleto.replace("‐", "-");
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
                return false;
            var tmp = rutCompleto.split('-');
            var digv = tmp[1];
            var rut = tmp[0];
            if (digv == 'K') digv = 'k';

            return (Fn.dv(rut) == digv);
        },
        dv: function (T) {
            var M = 0, S = 1;
            for (; T; T = Math.floor(T / 10))
                S = (S + T % 10 * (9 - M++ % 6)) % 11;
            return S ? S - 1 : 'k';
        }
    }


    $("#btnvalida").click(function () {
        if (Fn.validaRut($("#txt_rut").val())) {
            $("#msgerror").html(" ");
        } else {
            $("#msgerror").html("El Rut no es válido ");
        }
    });

    $("#msgerror").css("color", "#FF0000");






    $('#form').submit(function (event) {
        console.log("Formulario enviado")
        event.preventDefault();
    });

    if('geolocation' in navigator) {
        /* geolocation is available */
        console.log("available")
        navigator.geolocation.getCurrentPosition((position) => {
            console.log(position.coords.latitude);
            console.log(position.coords.longitude);
            $.get(`https://api.weatherapi.com/v1/current.json?q=${position.coords.latitude},${position.coords.longitude}&key=${weatherApiKey}`, 
            function(data) {
                console.log(data)
                $('#weather').html(`
                    <div class="weather">
                        <p>El clima en ${data.location.country}, ${data.location.region}</p>
                        <p><img src="https:${data.current.condition.icon}"/> ${data.current.temp_c}°C</p>
                    </div>
                `);
            })
        });
    } else {
        /* geolocation IS NOT available */
        console.log("not available")
    }



});