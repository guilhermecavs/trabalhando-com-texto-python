-- Filtro pandoc: converte divs de callout em ambientes tcolorbox no LaTeX.
-- No HTML, os divs (::: {.dica} etc.) sao mantidos e estilizados pelo CSS.
local envmap = {
  dica = "tipbox",
  nota = "notebox",
  atencao = "warnbox",
  objetivos = "objbox",
}

-- Remove caracteres invisiveis/zero-width (BOM e variation selector) que
-- aparecem em saidas coladas e junto de emojis; inofensivo nos dois formatos.
function Str(el)
  el.text = el.text:gsub("\u{FEFF}", ""):gsub("\u{FE0F}", "")
  return el
end

function Div(el)
  if not FORMAT:match("latex") then
    return el
  end
  for cls, env in pairs(envmap) do
    if el.classes:includes(cls) then
      local out = pandoc.List({})
      out:insert(pandoc.RawBlock("latex", "\\begin{" .. env .. "}"))
      out:extend(el.content)
      out:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
      return out
    end
  end
  return el
end
