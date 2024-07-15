---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Redstone - Documentation ^wODFynWe

Redstone - Documentation ^QYKGJhAp

local p = {}
function p.table( f )
	local args = f.args
	if args[1] == nil then
		args = f:getParent().args
	end
	local caption = args.caption or ''
	local captionstyle = args.captionstyle or ''
	local clear = args.clear or ''
	local float = args.float or ''
	local size = tonumber( args.size ) or 32
	local style = args.style or ''
	local tablestyle = args.tablestyle or ''
	local sprite = require( 'Module:Sprite' ).sprite
	local ids = mw.loadData( 'Module:Schematic/data' ).ids
	local titles = mw.loadData( 'Module:Schematic/titles' )
	local isTable = false
	if args[2] or '' ~= '' then
		isTable = true
	end
	local categories = {}
	
	if size ~= 32 then
		tablestyle = 'font-size:' .. size .. 'px;' .. tablestyle
	end
	
	local cols = 0
	local maxcols = 0
	local schematic = {}
	local title = ''
	for _, cell in ipairs( args ) do
		cell = mw.text.trim( cell )
		if isTable and cell ~= '-' then
			cols = cols + 1
			if cols > maxcols then
				maxcols = cols
			end
		end
		
		if cell == '' or cell == 'air' then
			if isTable then
				table.insert( schematic, '|' )
			else
				table.insert( schematic, '<br>' )
			end
		elseif isTable and cell == '-' then
			cols = 0
			
			table.insert( schematic, '|-' )
		else
			local layers = {}
			title = {}
			for layer in mw.text.gsplit( cell, '%s*+%s*' ) do
				local idData = ids[layer]
				if idData then
					local image, spriteCat = sprite{
						data = 'Schematic/data',
						iddata = idData,
						scale = size / 16
					}
					table.insert( layers, image )
					table.insert( categories, spriteCat )
					
					if titles[layer] then
						table.insert( title, 1, titles[layer] )
					end
				else
					table.insert( layers, '<span class="text">' .. layer .. '</span>' )
				end
			end
			if args.text then
				table.insert( layers, '<span class="text">' .. args.text .. '</span>' )
			end
			
			title = table.concat( title, ' over ' )
			layers = table.concat( layers, '' )
			if isTable then
				if layers ~= '' then
					layers = '| title="' .. title .. '" | <div>' .. layers .. '</div>'
				else
					layers = '|'
				end
			end
			
			table.insert( schematic, layers )
		end
	end

	local captionwidth = maxcols * ( size + 1 ) + 1

	if isTable then
		table.insert( schematic, 1, '{|' .. 'class="schematic" style="min-width:' .. captionwidth .. 'px;' .. tablestyle .. '"' )
		table.insert( schematic, '|}' )
	else
		if #schematic == 0 then
			table.insert( schematic, '<br>' )
		end
		table.insert( schematic, 1, '<span class="schematic" style="' .. tablestyle .. '" title="' .. title .. '">' )
		table.insert( schematic, '</span>' )
	end
	
	local out
	if caption ~= '' or float ~= '' then
		if float == '' then
			float = 'right'
		end
		if clear == '' then
			clear = 'none'
		end

		if captionwidth < 182 then
			captionwidth = 182
		end
		
		if not args.nohelp and mw.title.getCurrentTitle().prefixedText ~= 'Help:Schematic' then
			caption = '<span style="float:right;padding-left:0.5em">' ..
				f:expandTemplate{
					title = 'CommentSprite',
					args = {
						'1',
						link = 'Help:Schematic',
						title = 'Schematic help'
					}
				} ..
				'</span>' .. caption
		end
		
		out = {
			'<div class="thumb t' .. float .. '" style="overflow: auto; clear:' .. clear .. ';' .. style .. '">',
				'<div class="thumbinner" style="display:inline-block;min-width:' .. captionwidth .. 'px">\n',
					table.concat( schematic, '\n' ),
					'\n<div class="thumbcaption" style="max-width:' .. captionwidth .. 'px;' .. captionstyle .. '">\n' .. caption .. '</div>',
				'</div>',
			'</div>'
		}
		out = table.concat( out )
	else
		if isTable then
			out = table.concat( schematic, '\n' )
		else
			-- Inline schematic should be a single line
			out = table.concat( schematic )
		end
	end
	out = out:gsub( ' style=""', '' ):gsub( ' title=""%s*|?', '' )
	
	return out .. table.concat( categories )
end
return p
 ^AW9YtKuY

LUA ^xe8zdNVR

WikiText ^Q0yWZfTZ

{{Schematic
|input+A|rd-sw|air|air|-
|rd-nse|rs-e|rd-ew|output+O|-
|rd-nse|rs-e|SB||-
|input+B|rd-nw|air|air
}}

'''XOR Gate'''
 ^XmBj092T

2D - bitmap
(sprite) ^qWfrD4wA

@ minecraft.fandom.com ^Af8w28JP

Tools ^LAAQmXmu

Usage ^ELugJsMF

Output ^yBwwGzNJ

@kaaroCraft ^qDrslrpL

15th July 2024 ^wDJ9XQNM

# Embedded files
ac6a24bffed9aa5acbfc80ffe23dc7d5e385e012: [[Pasted Image 20240716011230_236.png]]
22f5da96403282b7c3c4f0659e98e4f6b0d64722: [[Pasted Image 20240716011230_263.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.7",
	"elements": [
		{
			"type": "rectangle",
			"version": 207,
			"versionNonce": 1353407046,
			"index": "bFT",
			"isDeleted": false,
			"id": "jNGQFuMkkAs0xgRUDL-jA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -463.71598197171716,
			"y": -744.1639338841278,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#8fca5c",
			"width": 680.950279433182,
			"height": 1051.7809927682554,
			"seed": 497938522,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 756,
			"versionNonce": 269754758,
			"index": "bFU",
			"isDeleted": false,
			"id": "WpmA2BlaDj0_V09nawrZ7",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -548.0624304665498,
			"y": -77.25962407725638,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#61371f",
			"width": 1019.6489578752368,
			"height": 335.34707447663794,
			"seed": 1711461658,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 533,
			"versionNonce": 1298268358,
			"index": "bFV",
			"isDeleted": false,
			"id": "tmbZ7FK_1v14rVcDRFWbg",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -548.0624304665498,
			"y": -284.4509395325522,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#854f2b",
			"width": 1021.1343247827601,
			"height": 193.54109108453136,
			"seed": 1138565594,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 364,
			"versionNonce": 1009907718,
			"index": "bFW",
			"isDeleted": false,
			"id": "qTslV2P2ebQR-jA40Nb29",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -548.253500049369,
			"y": -585.5203875163579,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#c28340",
			"width": 1017.2590690300028,
			"height": 284.63177092967834,
			"seed": 844093082,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 845,
			"versionNonce": 344000326,
			"index": "bFX",
			"isDeleted": false,
			"id": "wODFynWe",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -447.1219885946921,
			"y": -727.0309170316641,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#eebefa",
			"width": 627.1641845703125,
			"height": 60.47634697173298,
			"seed": 1376645978,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 48.381077577386385,
			"fontFamily": 1,
			"text": "Redstone - Documentation",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Redstone - Documentation",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 912,
			"versionNonce": 111947398,
			"index": "bFXV",
			"isDeleted": false,
			"id": "QYKGJhAp",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -445.6219885946921,
			"y": -727.0309170316641,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#eebefa",
			"width": 627.1641845703125,
			"height": 60.47634697173298,
			"seed": 896170010,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 48.381077577386385,
			"fontFamily": 1,
			"text": "Redstone - Documentation",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Redstone - Documentation",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 302,
			"versionNonce": 795897286,
			"index": "bFY",
			"isDeleted": false,
			"id": "BoAMFdFQNQeft8-EDdIPd",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 29.30706981205276,
			"y": -571.8508932594968,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#fff9db",
			"width": 155.06124240091322,
			"height": 255.62498531652818,
			"seed": 743990490,
			"groupIds": [
				"hjm_z1rpNiBqa56cDuocn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 603,
			"versionNonce": 199935238,
			"index": "bFZ",
			"isDeleted": false,
			"id": "AW9YtKuY",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": 42.16456751942496,
			"y": -567.0693721326179,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#eebefa",
			"width": 129.09375,
			"height": 246.06194306277033,
			"seed": 275429786,
			"groupIds": [
				"hjm_z1rpNiBqa56cDuocn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": "https://minecraft.fandom.com/wiki/Module:Schematic",
			"locked": false,
			"fontSize": 1.3670107947931684,
			"fontFamily": 3,
			"text": "local p = {}\nfunction p.table( f )\n\tlocal args = f.args\n\tif args[1] == nil then\n\t\targs = f:getParent().args\n\tend\n\tlocal caption = args.caption or ''\n\tlocal captionstyle = args.captionstyle or ''\n\tlocal clear = args.clear or ''\n\tlocal float = args.float or ''\n\tlocal size = tonumber( args.size ) or 32\n\tlocal style = args.style or ''\n\tlocal tablestyle = args.tablestyle or ''\n\tlocal sprite = require( 'Module:Sprite' ).sprite\n\tlocal ids = mw.loadData( 'Module:Schematic/data' ).ids\n\tlocal titles = mw.loadData( 'Module:Schematic/titles' )\n\tlocal isTable = false\n\tif args[2] or '' ~= '' then\n\t\tisTable = true\n\tend\n\tlocal categories = {}\n\t\n\tif size ~= 32 then\n\t\ttablestyle = 'font-size:' .. size .. 'px;' .. tablestyle\n\tend\n\t\n\tlocal cols = 0\n\tlocal maxcols = 0\n\tlocal schematic = {}\n\tlocal title = ''\n\tfor _, cell in ipairs( args ) do\n\t\tcell = mw.text.trim( cell )\n\t\tif isTable and cell ~= '-' then\n\t\t\tcols = cols + 1\n\t\t\tif cols > maxcols then\n\t\t\t\tmaxcols = cols\n\t\t\tend\n\t\tend\n\t\t\n\t\tif cell == '' or cell == 'air' then\n\t\t\tif isTable then\n\t\t\t\ttable.insert( schematic, '|' )\n\t\t\telse\n\t\t\t\ttable.insert( schematic, '<br>' )\n\t\t\tend\n\t\telseif isTable and cell == '-' then\n\t\t\tcols = 0\n\t\t\t\n\t\t\ttable.insert( schematic, '|-' )\n\t\telse\n\t\t\tlocal layers = {}\n\t\t\ttitle = {}\n\t\t\tfor layer in mw.text.gsplit( cell, '%s*+%s*' ) do\n\t\t\t\tlocal idData = ids[layer]\n\t\t\t\tif idData then\n\t\t\t\t\tlocal image, spriteCat = sprite{\n\t\t\t\t\t\tdata = 'Schematic/data',\n\t\t\t\t\t\tiddata = idData,\n\t\t\t\t\t\tscale = size / 16\n\t\t\t\t\t}\n\t\t\t\t\ttable.insert( layers, image )\n\t\t\t\t\ttable.insert( categories, spriteCat )\n\t\t\t\t\t\n\t\t\t\t\tif titles[layer] then\n\t\t\t\t\t\ttable.insert( title, 1, titles[layer] )\n\t\t\t\t\tend\n\t\t\t\telse\n\t\t\t\t\ttable.insert( layers, '<span class=\"text\">' .. layer .. '</span>' )\n\t\t\t\tend\n\t\t\tend\n\t\t\tif args.text then\n\t\t\t\ttable.insert( layers, '<span class=\"text\">' .. args.text .. '</span>' )\n\t\t\tend\n\t\t\t\n\t\t\ttitle = table.concat( title, ' over ' )\n\t\t\tlayers = table.concat( layers, '' )\n\t\t\tif isTable then\n\t\t\t\tif layers ~= '' then\n\t\t\t\t\tlayers = '| title=\"' .. title .. '\" | <div>' .. layers .. '</div>'\n\t\t\t\telse\n\t\t\t\t\tlayers = '|'\n\t\t\t\tend\n\t\t\tend\n\t\t\t\n\t\t\ttable.insert( schematic, layers )\n\t\tend\n\tend\n\n\tlocal captionwidth = maxcols * ( size + 1 ) + 1\n\n\tif isTable then\n\t\ttable.insert( schematic, 1, '{|' .. 'class=\"schematic\" style=\"min-width:' .. captionwidth .. 'px;' .. tablestyle .. '\"' )\n\t\ttable.insert( schematic, '|}' )\n\telse\n\t\tif #schematic == 0 then\n\t\t\ttable.insert( schematic, '<br>' )\n\t\tend\n\t\ttable.insert( schematic, 1, '<span class=\"schematic\" style=\"' .. tablestyle .. '\" title=\"' .. title .. '\">' )\n\t\ttable.insert( schematic, '</span>' )\n\tend\n\t\n\tlocal out\n\tif caption ~= '' or float ~= '' then\n\t\tif float == '' then\n\t\t\tfloat = 'right'\n\t\tend\n\t\tif clear == '' then\n\t\t\tclear = 'none'\n\t\tend\n\n\t\tif captionwidth < 182 then\n\t\t\tcaptionwidth = 182\n\t\tend\n\t\t\n\t\tif not args.nohelp and mw.title.getCurrentTitle().prefixedText ~= 'Help:Schematic' then\n\t\t\tcaption = '<span style=\"float:right;padding-left:0.5em\">' ..\n\t\t\t\tf:expandTemplate{\n\t\t\t\t\ttitle = 'CommentSprite',\n\t\t\t\t\targs = {\n\t\t\t\t\t\t'1',\n\t\t\t\t\t\tlink = 'Help:Schematic',\n\t\t\t\t\t\ttitle = 'Schematic help'\n\t\t\t\t\t}\n\t\t\t\t} ..\n\t\t\t\t'</span>' .. caption\n\t\tend\n\t\t\n\t\tout = {\n\t\t\t'<div class=\"thumb t' .. float .. '\" style=\"overflow: auto; clear:' .. clear .. ';' .. style .. '\">',\n\t\t\t\t'<div class=\"thumbinner\" style=\"display:inline-block;min-width:' .. captionwidth .. 'px\">\\n',\n\t\t\t\t\ttable.concat( schematic, '\\n' ),\n\t\t\t\t\t'\\n<div class=\"thumbcaption\" style=\"max-width:' .. captionwidth .. 'px;' .. captionstyle .. '\">\\n' .. caption .. '</div>',\n\t\t\t\t'</div>',\n\t\t\t'</div>'\n\t\t}\n\t\tout = table.concat( out )\n\telse\n\t\tif isTable then\n\t\t\tout = table.concat( schematic, '\\n' )\n\t\telse\n\t\t\t-- Inline schematic should be a single line\n\t\t\tout = table.concat( schematic )\n\t\tend\n\tend\n\tout = out:gsub( ' style=\"\"', '' ):gsub( ' title=\"\"%s*|?', '' )\n\t\n\treturn out .. table.concat( categories )\nend\nreturn p\n",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "local p = {}\nfunction p.table( f )\n\tlocal args = f.args\n\tif args[1] == nil then\n\t\targs = f:getParent().args\n\tend\n\tlocal caption = args.caption or ''\n\tlocal captionstyle = args.captionstyle or ''\n\tlocal clear = args.clear or ''\n\tlocal float = args.float or ''\n\tlocal size = tonumber( args.size ) or 32\n\tlocal style = args.style or ''\n\tlocal tablestyle = args.tablestyle or ''\n\tlocal sprite = require( 'Module:Sprite' ).sprite\n\tlocal ids = mw.loadData( 'Module:Schematic/data' ).ids\n\tlocal titles = mw.loadData( 'Module:Schematic/titles' )\n\tlocal isTable = false\n\tif args[2] or '' ~= '' then\n\t\tisTable = true\n\tend\n\tlocal categories = {}\n\t\n\tif size ~= 32 then\n\t\ttablestyle = 'font-size:' .. size .. 'px;' .. tablestyle\n\tend\n\t\n\tlocal cols = 0\n\tlocal maxcols = 0\n\tlocal schematic = {}\n\tlocal title = ''\n\tfor _, cell in ipairs( args ) do\n\t\tcell = mw.text.trim( cell )\n\t\tif isTable and cell ~= '-' then\n\t\t\tcols = cols + 1\n\t\t\tif cols > maxcols then\n\t\t\t\tmaxcols = cols\n\t\t\tend\n\t\tend\n\t\t\n\t\tif cell == '' or cell == 'air' then\n\t\t\tif isTable then\n\t\t\t\ttable.insert( schematic, '|' )\n\t\t\telse\n\t\t\t\ttable.insert( schematic, '<br>' )\n\t\t\tend\n\t\telseif isTable and cell == '-' then\n\t\t\tcols = 0\n\t\t\t\n\t\t\ttable.insert( schematic, '|-' )\n\t\telse\n\t\t\tlocal layers = {}\n\t\t\ttitle = {}\n\t\t\tfor layer in mw.text.gsplit( cell, '%s*+%s*' ) do\n\t\t\t\tlocal idData = ids[layer]\n\t\t\t\tif idData then\n\t\t\t\t\tlocal image, spriteCat = sprite{\n\t\t\t\t\t\tdata = 'Schematic/data',\n\t\t\t\t\t\tiddata = idData,\n\t\t\t\t\t\tscale = size / 16\n\t\t\t\t\t}\n\t\t\t\t\ttable.insert( layers, image )\n\t\t\t\t\ttable.insert( categories, spriteCat )\n\t\t\t\t\t\n\t\t\t\t\tif titles[layer] then\n\t\t\t\t\t\ttable.insert( title, 1, titles[layer] )\n\t\t\t\t\tend\n\t\t\t\telse\n\t\t\t\t\ttable.insert( layers, '<span class=\"text\">' .. layer .. '</span>' )\n\t\t\t\tend\n\t\t\tend\n\t\t\tif args.text then\n\t\t\t\ttable.insert( layers, '<span class=\"text\">' .. args.text .. '</span>' )\n\t\t\tend\n\t\t\t\n\t\t\ttitle = table.concat( title, ' over ' )\n\t\t\tlayers = table.concat( layers, '' )\n\t\t\tif isTable then\n\t\t\t\tif layers ~= '' then\n\t\t\t\t\tlayers = '| title=\"' .. title .. '\" | <div>' .. layers .. '</div>'\n\t\t\t\telse\n\t\t\t\t\tlayers = '|'\n\t\t\t\tend\n\t\t\tend\n\t\t\t\n\t\t\ttable.insert( schematic, layers )\n\t\tend\n\tend\n\n\tlocal captionwidth = maxcols * ( size + 1 ) + 1\n\n\tif isTable then\n\t\ttable.insert( schematic, 1, '{|' .. 'class=\"schematic\" style=\"min-width:' .. captionwidth .. 'px;' .. tablestyle .. '\"' )\n\t\ttable.insert( schematic, '|}' )\n\telse\n\t\tif #schematic == 0 then\n\t\t\ttable.insert( schematic, '<br>' )\n\t\tend\n\t\ttable.insert( schematic, 1, '<span class=\"schematic\" style=\"' .. tablestyle .. '\" title=\"' .. title .. '\">' )\n\t\ttable.insert( schematic, '</span>' )\n\tend\n\t\n\tlocal out\n\tif caption ~= '' or float ~= '' then\n\t\tif float == '' then\n\t\t\tfloat = 'right'\n\t\tend\n\t\tif clear == '' then\n\t\t\tclear = 'none'\n\t\tend\n\n\t\tif captionwidth < 182 then\n\t\t\tcaptionwidth = 182\n\t\tend\n\t\t\n\t\tif not args.nohelp and mw.title.getCurrentTitle().prefixedText ~= 'Help:Schematic' then\n\t\t\tcaption = '<span style=\"float:right;padding-left:0.5em\">' ..\n\t\t\t\tf:expandTemplate{\n\t\t\t\t\ttitle = 'CommentSprite',\n\t\t\t\t\targs = {\n\t\t\t\t\t\t'1',\n\t\t\t\t\t\tlink = 'Help:Schematic',\n\t\t\t\t\t\ttitle = 'Schematic help'\n\t\t\t\t\t}\n\t\t\t\t} ..\n\t\t\t\t'</span>' .. caption\n\t\tend\n\t\t\n\t\tout = {\n\t\t\t'<div class=\"thumb t' .. float .. '\" style=\"overflow: auto; clear:' .. clear .. ';' .. style .. '\">',\n\t\t\t\t'<div class=\"thumbinner\" style=\"display:inline-block;min-width:' .. captionwidth .. 'px\">\\n',\n\t\t\t\t\ttable.concat( schematic, '\\n' ),\n\t\t\t\t\t'\\n<div class=\"thumbcaption\" style=\"max-width:' .. captionwidth .. 'px;' .. captionstyle .. '\">\\n' .. caption .. '</div>',\n\t\t\t\t'</div>',\n\t\t\t'</div>'\n\t\t}\n\t\tout = table.concat( out )\n\telse\n\t\tif isTable then\n\t\t\tout = table.concat( schematic, '\\n' )\n\t\telse\n\t\t\t-- Inline schematic should be a single line\n\t\t\tout = table.concat( schematic )\n\t\tend\n\tend\n\tout = out:gsub( ' style=\"\"', '' ):gsub( ' title=\"\"%s*|?', '' )\n\t\n\treturn out .. table.concat( categories )\nend\nreturn p\n",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 323,
			"versionNonce": 1838691398,
			"index": "bFa",
			"isDeleted": false,
			"id": "xe8zdNVR",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 146.20396403914856,
			"y": -564.4144727354296,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#fff9db",
			"width": 28.125,
			"height": 19.2,
			"seed": 282359386,
			"groupIds": [
				"hjm_z1rpNiBqa56cDuocn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 3,
			"text": "LUA",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "LUA",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 244,
			"versionNonce": 1851112326,
			"index": "bFb",
			"isDeleted": false,
			"id": "Q0yWZfTZ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -177.8836036145767,
			"y": -345.96233411207595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#fff9db",
			"width": 109.734375,
			"height": 28.1015466073755,
			"seed": 2120784666,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 23.41795550614625,
			"fontFamily": 3,
			"text": "WikiText",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "WikiText",
			"lineHeight": 1.2
		},
		{
			"type": "line",
			"version": 1157,
			"versionNonce": 1684036294,
			"index": "bFc",
			"isDeleted": false,
			"id": "4Slq9BRiFlZOBgWmMkyZk",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -261.4078642878312,
			"y": -418.0963075149384,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#fff9db",
			"width": 279.4979545884353,
			"height": 76.57158650227757,
			"seed": 395978714,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					45.786143639890724,
					2.662266520437697
				],
				[
					101.35052009665287,
					71.65754420655503
				],
				[
					181.78691849061397,
					72.26395501789375
				],
				[
					210.0132263718915,
					18.991470370616298
				],
				[
					278.1404254674726,
					-3.8100462216298183
				],
				[
					136.50824457730505,
					72.37207477495576
				],
				[
					-1.3575291209626812,
					-4.199511727321806
				],
				[
					0,
					0
				]
			]
		},
		{
			"type": "rectangle",
			"version": 206,
			"versionNonce": 1448415750,
			"index": "bFd",
			"isDeleted": false,
			"id": "r0EYwKXYfbzAhMz2UnMCC",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -258.625454620239,
			"y": -270.38412979832447,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#e7f5ff",
			"width": 271.49298073749287,
			"height": 163.10987852094695,
			"seed": 1417419930,
			"groupIds": [
				"RjPbTsZw2xXX2D7wGxBK7"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 492,
			"versionNonce": 1865474374,
			"index": "bFe",
			"isDeleted": false,
			"id": "XmBj092T",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -242.16412050149302,
			"y": -264.69522405517364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#fff9db",
			"width": 238.5703125,
			"height": 151.7320670346441,
			"seed": 851540314,
			"groupIds": [
				"RjPbTsZw2xXX2D7wGxBK7"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 14.049265466170752,
			"fontFamily": 3,
			"text": "{{Schematic\n|input+A|rd-sw|air|air|-\n|rd-nse|rs-e|rd-ew|output+O|-\n|rd-nse|rs-e|SB||-\n|input+B|rd-nw|air|air\n}}\n\n'''XOR Gate'''\n",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "{{Schematic\n|input+A|rd-sw|air|air|-\n|rd-nse|rs-e|rd-ew|output+O|-\n|rd-nse|rs-e|SB||-\n|input+B|rd-nw|air|air\n}}\n\n'''XOR Gate'''\n",
			"lineHeight": 1.2
		},
		{
			"type": "image",
			"version": 165,
			"versionNonce": 1917896838,
			"index": "bFf",
			"isDeleted": false,
			"id": "JuGmXXj5E7hkV9zz0kMhh",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -263.40157350968275,
			"y": -66.43723262532694,
			"strokeColor": "transparent",
			"backgroundColor": "#e7f5ff",
			"width": 281.0452185163811,
			"height": 321.7228159332257,
			"seed": 29179418,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"status": "saved",
			"fileId": "ac6a24bffed9aa5acbfc80ffe23dc7d5e385e012",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 126,
			"versionNonce": 795985862,
			"index": "bFg",
			"isDeleted": false,
			"id": "xL8HScQ9L27yuoFTWCajn",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -436.14749386256335,
			"y": -547.1847263297977,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"width": 170.31178983082918,
			"height": 199.6425941744801,
			"seed": 778201818,
			"groupIds": [
				"lNZJpnMFomBWBNyBAKE95"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false
		},
		{
			"type": "image",
			"version": 188,
			"versionNonce": 1991302918,
			"index": "bFh",
			"isDeleted": false,
			"id": "X-oDwjKKMiQolZbIy1uID",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 2,
			"opacity": 100,
			"angle": 0,
			"x": -426.42842784673485,
			"y": -501.77281909172325,
			"strokeColor": "transparent",
			"backgroundColor": "#eebefa",
			"width": 144.42179402816885,
			"height": 144.42179402816885,
			"seed": 256114586,
			"groupIds": [
				"lNZJpnMFomBWBNyBAKE95"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"status": "saved",
			"fileId": "22f5da96403282b7c3c4f0659e98e4f6b0d64722",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 348,
			"versionNonce": 210439750,
			"index": "bFi",
			"isDeleted": false,
			"id": "qWfrD4wA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -422.0723929532269,
			"y": -540.4402856563765,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#e7f5ff",
			"width": 77.54174065361228,
			"height": 28.880892996805645,
			"seed": 815070298,
			"groupIds": [
				"lNZJpnMFomBWBNyBAKE95"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 12.033705415335683,
			"fontFamily": 3,
			"text": "2D - bitmap\n(sprite)",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2D - bitmap\n(sprite)",
			"lineHeight": 1.2
		},
		{
			"type": "text",
			"version": 304,
			"versionNonce": 501044614,
			"index": "bFj",
			"isDeleted": false,
			"id": "Af8w28JP",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -444.0331484151302,
			"y": -674.344197830228,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 322.5671691894531,
			"height": 35.38223310201049,
			"seed": 539517210,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 28.305786481608394,
			"fontFamily": 1,
			"text": "@ minecraft.fandom.com",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "@ minecraft.fandom.com",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 414,
			"versionNonce": 870626502,
			"index": "bFk",
			"isDeleted": false,
			"id": "LAAQmXmu",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.535386414819479,
			"x": 245.92706639289372,
			"y": -468.338847732889,
			"strokeColor": "#ffffff",
			"backgroundColor": "#fff9db",
			"width": 209.8024139404297,
			"height": 96.49298072411354,
			"seed": 963718618,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 77.19438457929083,
			"fontFamily": 1,
			"text": "Tools",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Tools",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 546,
			"versionNonce": 675163142,
			"index": "bFl",
			"isDeleted": false,
			"id": "ELugJsMF",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.535386414819479,
			"x": 236.1239352893781,
			"y": -236.63710331685525,
			"strokeColor": "#ffffff",
			"backgroundColor": "#fff9db",
			"width": 229.40867614746094,
			"height": 96.49298072411354,
			"seed": 1904370330,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 77.19438457929083,
			"fontFamily": 1,
			"text": "Usage",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Usage",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 574,
			"versionNonce": 417774406,
			"index": "bFm",
			"isDeleted": false,
			"id": "yBwwGzNJ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.535386414819479,
			"x": 216.32470280646794,
			"y": 25.02067103346235,
			"strokeColor": "#ffffff",
			"backgroundColor": "#fff9db",
			"width": 269.00714111328125,
			"height": 96.49298072411354,
			"seed": 588185434,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 77.19438457929083,
			"fontFamily": 1,
			"text": "Output",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Output",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 831,
			"versionNonce": 1547395718,
			"index": "bFn",
			"isDeleted": false,
			"id": "qDrslrpL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 78.45468740917113,
			"y": 270.1812858205285,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#61371f",
			"width": 134.7014923095703,
			"height": 26.35912996764845,
			"seed": 1516897306,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 21.08730397411876,
			"fontFamily": 1,
			"text": "@kaaroCraft",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "@kaaroCraft",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 1019,
			"versionNonce": 1962484166,
			"index": "bFo",
			"isDeleted": false,
			"id": "wDJ9XQNM",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -440.90166007147855,
			"y": -617.4683302541662,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#61371f",
			"width": 126.46268463134766,
			"height": 20.70779107131344,
			"seed": 562458842,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1721072549938,
			"link": null,
			"locked": false,
			"fontSize": 16.566232857050753,
			"fontFamily": 1,
			"text": "15th July 2024",
			"rawText": "",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "15th July 2024",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 787,
		"scrollY": 1099.7265625,
		"zoom": {
			"value": 1
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		},
		"objectsSnapModeEnabled": false
	},
	"files": {}
}
```
%%