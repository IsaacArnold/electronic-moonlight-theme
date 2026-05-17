# Rider Syntax Color Alignment Design

**Date:** 2026-05-15
**Status:** Approved

## Goal

Align the Rider/JetBrains color scheme with the VS Code theme's syntax highlighting. The VS Code `tokenColors` array has late-override rules whose colors were never carried into the Rider `.icls` files, and the Rider files are missing JS/TS language-specific attribute blocks entirely.

## Files Changed

Both files must be kept in sync:
- `jetbrains/Electronic Moonlight.icls`
- `jetbrains-plugin/src/main/resources/colors/Electronic Moonlight.icls`

## Part 1: Color Fixes to Existing Attributes

These attributes already exist in the `.icls` but use the wrong color value. The "VS Code source" column shows which TextMate scope rule (or final override) defines the correct color.

| Attribute(s) | From | To | VS Code source |
|---|---|---|---|
| `LOCAL_VARIABLE`, `REASSIGNED_LOCAL_VARIABLE_ATTRIBUTES` | `#C8D3F5` | `#E26674` | `variable` (final override, line ~1474) |
| `ReSharper.ReSharperLOCAL_VARIABLE_IDENTIFIER` | `#C8D3F5` | `#E26674` | same |
| `ReSharper.ReSharperMUTABLE_LOCAL_VARIABLE_IDENTIFIER` | `#C8D3F5` | `#E26674` | same |
| `ReSharper.ReSharperCAPTURED_VARIABLE_IDENTIFIER` | `#C8D3F5` | `#E26674` | same |
| `FUNCTION_CALL` | `#82AAFF` | `#65BCFF` | `support.function` / `meta.function-call entity.name.function` |
| `CONSTANT` | `#FF98A4` | `#E76572` | `support.constant` (final override — built-in/library constants) |
| `ENUM_CONST_ATTRIBUTES` | `#FF98A4` | `#E76572` | same — enum members are user-defined but follow the same visual treatment |
| `HTML_ATTRIBUTE_VALUE`, `XML_ATTRIBUTE_VALUE` | `#C3E88D` | `#56A3B1` | `string.quoted.double.html` |

Note: `STRING` stays `#C3E88D`. VS Code intentionally colors HTML/XML attribute string values differently (teal-blue) from regular strings (green).

## Part 2: New Language-Specific Attribute Blocks

### JavaScript / TypeScript

These cover the VS Code meta scopes (`meta.var.expr.ts`, `meta.block.ts`, `meta.function.ts`) — Rider handles those contexts via its own JS/TS semantic attributes rather than TextMate meta scopes.

| Attribute | Color | Font style | Maps to VS Code scope |
|---|---|---|---|
| `JAVA_SCRIPT_LOCAL_VARIABLE` | `#E26674` | — | `variable` / `meta.var.expr.ts` |
| `JAVA_SCRIPT_GLOBAL_VARIABLE` | `#FFC777` | — | `support.variable.dom` / `support.type.object.module` |
| `JAVA_SCRIPT_PARAMETER` | `#FCA7EA` | — | `variable.parameter` |
| `JAVA_SCRIPT_INSTANCE_MEMBER_VARIABLE` | `#A9B8E8` | — | `variable.other.object.property` |
| `JAVA_SCRIPT_STATIC_MEMBER_VARIABLE` | `#FF966C` | — | `variable.other.constant` (static context) |
| `JAVA_SCRIPT_FUNCTION_DECLARATION` | `#82AAFF` | — | `entity.name.function` |
| `JAVA_SCRIPT_INSTANCE_MEMBER_FUNCTION` | `#82AAFF` | — | `entity.name.method.js` |
| `JAVA_SCRIPT_STATIC_MEMBER_FUNCTION` | `#82AAFF` | — | same |
| `JAVA_SCRIPT_KEYWORD` | `#C099FF` | italic | `keyword` / `keyword.control` |
| `JAVA_SCRIPT_REGEXP` | `#B4F9F8` | — | `string.regexp` |
| `JAVA_SCRIPT_VALID_STRING_ESCAPE` | `#86E1FC` | — | `constant.character.escape` |
| `JAVA_SCRIPT_TEMPLATE_LITERAL` | `#86E1FC` | — | `punctuation.definition.template-expression` |
| `JAVA_SCRIPT_MODULE_NAME` | `#C3E88D` | — | `string` (import paths) |

### CSS

| Attribute | Color | Maps to VS Code scope |
|---|---|---|
| `CSS_UNIT` | `#D59DF6` | `keyword.other.unit.px.css` |

### HTML / Razor

No new attributes needed — the `HTML_ATTRIBUTE_VALUE` color fix in Part 1 covers the outstanding gap.

## Out of Scope

- UI/IDE chrome colors (toolbars, tabs, panels) — covered by the separate theme.json
- Markdown attributes — already aligned
- Other languages (Python, Go, Kotlin, etc.) — not used in Rider by this user
