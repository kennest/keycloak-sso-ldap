<#-- Hérite des messages d’internationalisation -->
<#assign usernameLabel = msg("username")!>
<#assign passwordLabel = msg("password")!>
<#assign forgotPassword = msg("doForgotPassword")!>
<#assign loginButton = msg("doLogIn")!>

<form id="kc-form-login" class="custom-login-form" onsubmit="login.disabled = true; return true;" action="${url.loginAction}" method="post">
    <#-- Message d’accueil personnalisé -->
    <div class="login-form-title">
        <h3>Connecte-toi à ta plateforme sécurisée</h3>
        <p>Bienvenue ! Veuillez utiliser vos identifiants pour vous connecter.</p>
    </div>
    <div class="form-group">
        <label for="username">${usernameLabel}</label>
        <input tabindex="1" id="username" class="form-control" name="username" value="${(login.username!'')}" type="text" autofocus autocomplete="username" />
    </div>
    <div class="form-group">
        <label for="password">${passwordLabel}</label>
        <input tabindex="2" id="password" class="form-control" name="password" type="password" autocomplete="current-password" />
    </div>
    <#if realm.resetPasswordAllowed>
        <div class="form-group">
            <a href="${url.loginResetCredentialsUrl}" class="forgot-password-link">${forgotPassword}</a>
        </div>
    </#if>
    <div class="form-group">
        <button tabindex="3" class="btn btn-primary btn-block" name="login" id="kc-login">${loginButton}</button>
    </div>
    <#-- Message d’erreur éventuel -->
    <#if message?has_content && (message.type == "error")>
        <div class="alert alert-danger">${message.summary}</div>
    </#if>
</form>