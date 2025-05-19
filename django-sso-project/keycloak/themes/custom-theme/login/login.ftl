<#import "template.ftl" as layout>
<@layout.registrationLayout displayInfo=false displayMessage=true; section>
    <div class="kc-logo-title">
        <img src="${url.resourcesPath}/img/logo.png" alt="Logo" style="max-width:150px;">
        <h2>Bienvenue sur Ma Plateforme</h2>
    </div>
    <#-- Affiche le formulaire de connexion -->
    <#include "login-form.ftl">
</@layout.registrationLayout>